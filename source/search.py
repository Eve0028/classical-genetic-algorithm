import optuna
import benchmark_functions as bf

from source.evolution.evolution import Evolution
from source.evolution.strategies import SelectionStrategyEnum, CrossoverStrategyEnum, MutationStrategyEnum
from source.inversion.inversion import Inversion
from source.population.population import Population


def objective(trial):
    population_size = trial.suggest_int('population_size', 10, 1000)
    num_generations = trial.suggest_int('num_generations', 10, 1000)

    num_variables = trial.suggest_int('num_variables', 2, 2)
    function = bf.Hypersphere(num_variables)
    search_minimum = True
    precision = trial.suggest_int('precision', 2, 5)
    start_interval = -5
    end_interval = 5

    selection_strategy_type = trial.suggest_categorical('selection_strategy', ['ROULETTE', 'TOURNAMENT', 'BEST'])
    selection_size = trial.suggest_int('selection_size', 2,
                                       population_size) if selection_strategy_type != 'TOURNAMENT' else None
    tournament_size = trial.suggest_int('tournament_size', 2,
                                        population_size // 2) if selection_strategy_type == 'TOURNAMENT' else None
    selection_strategy = SelectionStrategyEnum[selection_strategy_type].value(
        selection_size if selection_size else tournament_size)

    elite_strategy = trial.suggest_categorical('elite_strategy', [True, False])
    elite_size = trial.suggest_int('elite_size', 1, population_size // 2) if elite_strategy else 0

    crossover_strategy_type = trial.suggest_categorical('crossover_strategy', ['POINT', 'DISCRETE', 'UNIFORM'])
    crossover_probability = trial.suggest_float('crossover_probability', 0.1, 1.0)
    intersection_number = trial.suggest_int('intersection_number', 1, 2) if crossover_strategy_type in ['POINT'] else None
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
    evolution.evolve()

    best_individual = min(evolution.individuals, key=lambda x: function(x))
    return function(best_individual)


study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=100)

print("Best parameters: ", study.best_params)
