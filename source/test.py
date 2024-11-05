import optuna
import benchmark_functions as bf

from source.evolution.evolution import Evolution
from source.evolution.strategies import SelectionStrategyEnum, CrossoverStrategyEnum, MutationStrategyEnum
from source.inversion.inversion import Inversion
from source.population.population import Population

best_ind = None


def objective(trial):
    global best_ind

    population_size = trial.suggest_int('population_size', 100, 100)
    num_generations = trial.suggest_int('num_generations', 1000, 1000)

    num_variables = trial.suggest_int('num_variables', 3, 3)
    function = bf.Hypersphere(num_variables)
    # function = bf.Schwefel(num_variables)
    search_minimum = True
    precision = trial.suggest_int('precision', 4, 4)
    start_interval = -5
    end_interval = 5

    selection_strategy_type = trial.suggest_categorical('selection_strategy', ['TOURNAMENT'])
    selection_size = trial.suggest_int('selection_size', 50,
                                       50) if selection_strategy_type != 'TOURNAMENT' else None
    tournament_size = trial.suggest_int('tournament_size', 4,
                                        4) if selection_strategy_type == 'TOURNAMENT' else None
    selection_strategy = SelectionStrategyEnum[selection_strategy_type].value(
        selection_size if selection_size else tournament_size)

    elite_strategy = trial.suggest_categorical('elite_strategy', [True])
    elite_size = trial.suggest_int('elite_size', 2, 2) if elite_strategy else 0

    crossover_strategy_type = trial.suggest_categorical('crossover_strategy', ['UNIFORM'])
    crossover_probability = trial.suggest_float('crossover_probability', 0.8, 0.8)
    intersection_number = trial.suggest_int('intersection_number', 2, 2) if crossover_strategy_type in [
        'POINT'] else None
    crossover_size = population_size - elite_size
    if crossover_strategy_type == 'POINT':
        crossover_strategy = CrossoverStrategyEnum[crossover_strategy_type].value(intersection_number, crossover_size,
                                                                                  crossover_probability)
    else:
        crossover_strategy = CrossoverStrategyEnum[crossover_strategy_type].value(crossover_size,
                                                                                  crossover_probability)

    mutation_strategy_type = trial.suggest_categorical('mutation_strategy', ['TWO_POINT'])
    mutation_probability = trial.suggest_float('mutation_probability', 0.2, 0.2)
    mutation_strategy = MutationStrategyEnum[mutation_strategy_type].value(mutation_probability)

    inversion = None
    is_inversion = trial.suggest_categorical('inversion', [True])
    if is_inversion:
        inversion_probability = trial.suggest_float('inversion_probability', 0.1, 0.1)
        inversion = Inversion(inversion_probability)

    population = Population(population_size, num_variables, precision=precision,
                            start_interval=start_interval, end_interval=end_interval,
                            generate=True)

    first_best_ind = min(population.individuals, key=lambda x: function(x.decode_chromosomes_representation()))
    print("First best individual: ", first_best_ind.chromosomes if first_best_ind else None)
    print("First ind values: ", first_best_ind.decode_chromosomes_representation() if first_best_ind else None)

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

    best_ind = min(evolution.individuals, key=lambda x: function(x.decode_chromosomes_representation()))
    return function(best_ind.decode_chromosomes_representation())


study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=1)

print("Best parameters: ", study.best_params)
print("Best individual: ", best_ind.chromosomes if best_ind else None)
print("Best ind values: ", best_ind.decode_chromosomes_representation() if best_ind else None)
