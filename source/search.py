import optuna
import time
from functools import partial

from source.evolution.evolution import Evolution
from source.evolution.functions import SimpleFunctionEnum
from source.evolution.strategies import SelectionStrategyEnum, CrossoverStrategyEnum, MutationStrategyEnum
from source.inversion.inversion import Inversion
from source.config.params import SIMPLE_FUNCTION_NAMES, NUM_VARIABLES, PRECISIONS, ACTUAL_DB_FILE_FULLNAME
from source.population.population import Population
from source.config.logging_config import logger


def objective(trial, function_name, num_variables, precision):
    trial.set_user_attr('function_name', function_name)
    trial.set_user_attr('num_variables', num_variables)
    trial.set_user_attr('precision', precision)

    population_size = trial.suggest_int('population_size', 100, 10000)
    num_generations = trial.suggest_int('num_generations', 100, 10000)

    function = SimpleFunctionEnum[function_name].value[0](num_variables)
    start_interval = SimpleFunctionEnum[function_name].value[1]
    end_interval = SimpleFunctionEnum[function_name].value[2]
    search_minimum = True

    selection_strategy_type = trial.suggest_categorical('selection_strategy', ['ROULETTE', 'TOURNAMENT', 'BEST'])
    selection_size = trial.suggest_int('selection_size', 10,
                                       population_size) if selection_strategy_type != 'TOURNAMENT' else None
    tournament_size = trial.suggest_int('tournament_size', 2,
                                        population_size // 2) if selection_strategy_type == 'TOURNAMENT' else None
    selection_strategy = SelectionStrategyEnum[selection_strategy_type].value(
        selection_size if selection_size else tournament_size)

    elite_strategy = trial.suggest_categorical('elite_strategy', [True, False])
    elite_size = trial.suggest_int('elite_size', 1, 10) if elite_strategy else 0

    crossover_strategy_type = trial.suggest_categorical('crossover_strategy', ['POINT', 'DISCRETE', 'UNIFORM'])
    crossover_probability = trial.suggest_float('crossover_probability', 0.5, 1.0)
    intersection_number = trial.suggest_int('intersection_number', 1, 2) if crossover_strategy_type in [
        'POINT'] else None
    crossover_size = population_size - elite_size
    if crossover_strategy_type == 'POINT':
        crossover_strategy = CrossoverStrategyEnum[crossover_strategy_type].value(intersection_number, crossover_size,
                                                                                  crossover_probability)
    else:
        crossover_strategy = CrossoverStrategyEnum[crossover_strategy_type].value(crossover_size,
                                                                                  crossover_probability)

    mutation_strategy_type = trial.suggest_categorical('mutation_strategy', ['ONE_POINT', 'TWO_POINT', 'BOUNDARY'])
    mutation_probability = trial.suggest_float('mutation_probability', 0.01, 0.5)
    mutation_strategy = MutationStrategyEnum[mutation_strategy_type].value(mutation_probability)

    inversion = None
    is_inversion = trial.suggest_categorical('inversion', [True, False])
    if is_inversion:
        inversion_probability = trial.suggest_float('inversion_probability', 0.01, 0.5)
        inversion = Inversion(inversion_probability)

    population = Population(population_size, num_variables, precision=precision,
                            start_interval=start_interval, end_interval=end_interval,
                            generate=True)

    logger.info(f"Evolution initialized with the following parameters:\n"
                f"function_name: {function_name}\n"
                f"num_variables: {num_variables}\n"
                f"precision: {precision}\n"
                f"population_size: {population_size}\n"
                f"number_of_generations: {num_generations}\n"
                f"selection_strategy: {selection_strategy_type}\n"
                f"selection_size: {selection_size}\n"
                f"tournament_size: {tournament_size}\n"
                f"elite_strategy: {elite_strategy}\n"
                f"elite_size: {elite_size}\n"
                f"crossover_strategy: {crossover_strategy_type}\n"
                f"crossover_probability: {crossover_probability}\n"
                f"intersection_number: {intersection_number}\n"
                f"mutation_strategy: {mutation_strategy_type}\n"
                f"mutation_probability: {mutation_probability}\n"
                f"inversion: {is_inversion}\n"
                f"inversion_probability: {inversion_probability if is_inversion else "None"}\n")

    evolution = Evolution(
        individuals=population.individuals,
        number_of_generations=num_generations,
        fitness_function=function,
        search_minimum=search_minimum,
        selection_strategy=selection_strategy,
        crossover_strategy=crossover_strategy,
        mutation_strategy=mutation_strategy,
        inversion=inversion,
        elitism_size=elite_size
    )
    start_time = time.time()
    evolution.evolve()
    end_time = time.time()
    computation_time = end_time - start_time
    logger.info(f"Computation time: {computation_time}")
    trial.set_user_attr('computation_time', computation_time)

    best_individual = min(evolution.individuals, key=lambda x: function(x.decode_chromosomes_representation()))
    logger.info(f"Chromosomes: {best_individual.chromosomes}")

    chromosomes_repr = best_individual.decode_chromosomes_representation()
    logger.info(f"Chromosomes representation values: {chromosomes_repr}")
    for i, chromosome in enumerate(best_individual.chromosomes):
        trial.set_user_attr(f'best_individual_chromosome_{i}_value', chromosomes_repr[i])

    return function(best_individual.decode_chromosomes_representation())


database_url = ACTUAL_DB_FILE_FULLNAME


def enqueue_running_and_failed_trials(study):
    trials = study.get_trials(deepcopy=False)
    # Set to store unique sample parameters
    enqueued_params = set()

    for trial in trials:
        if trial.state in [optuna.trial.TrialState.RUNNING, optuna.trial.TrialState.FAIL]:
            trial_params = tuple(trial.params.items())  # Replace the parameter dictionary with a tuple

            # Check that the parameters have not already been added to the queue
            if trial_params not in enqueued_params:
                print(f"Enqueuing trial with parameters: {trial.params}")
                study.enqueue_trial(trial.params)
                enqueued_params.add(trial_params)


for function_name in SIMPLE_FUNCTION_NAMES:
    for num_variable in NUM_VARIABLES:
        for precision in PRECISIONS:
            print(f"Optimizing {function_name} with {num_variable} variables and precision {precision}")

            study = optuna.create_study(
                study_name=f'{function_name}__var_{num_variable}__prec_{precision}',
                direction='minimize',
                storage=database_url,
                load_if_exists=True
            )

            enqueue_running_and_failed_trials(study)

            partial_objective = partial(objective, function_name=function_name, num_variables=num_variable,
                                        precision=precision)
            study.optimize(partial_objective, n_trials=30)

            print(
                f"Best parameters for {function_name}, num variables {num_variable}, precision {precision}: {study.best_params}")
            best_trial = study.best_trial
            print('Best individual: ')
            for i in range(num_variable):
                print(f'Chromosome {i}:', best_trial.user_attrs[f'best_individual_chromosome_{i}_value'])
            print(f'Computation time:', best_trial.user_attrs['computation_time'])

# cd source
# optuna-dashboard sqlite:///simple_functions.db
