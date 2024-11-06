from source.evolution.evolution import Evolution
from source.evolution.functions import SimpleFunctionEnum
from source.evolution.strategies import SelectionStrategyEnum, CrossoverStrategyEnum, MutationStrategyEnum
from source.gui.application import Application
from source.inversion.inversion import Inversion
from source.population.population import Population
import time


def start_algorithm() -> None:
    config = app.get_algorithm_config()
    population_size = config['population_size']
    num_generations = config['generations']
    num_variables = config['number_of_variables']
    precision = config['bits_count']
    search_minimum = config['search_minimum']
    start_interval = config['start_interval']
    end_interval = config['end_interval']

    function_name = 'HYPERSPHERE'
    function = SimpleFunctionEnum[function_name].value[0](num_variables)

    selection_strategy_type = config['selection_strategy']
    selection_size = config['individuals_best'] if selection_strategy_type != 'TOURNAMENT' else None
    tournament_size = config['individuals_best'] if selection_strategy_type == 'TOURNAMENT' else None
    selection_strategy = SelectionStrategyEnum[selection_strategy_type].value(
        selection_size if selection_size else tournament_size)

    elite_strategy = config['individuals_elite'] is not None
    elite_size = config['individuals_elite'] if elite_strategy else 0

    crossover_strategy_type = config['cross_strategy']
    crossover_probability = config['cross_prob']
    intersection_number = 2 if crossover_strategy_type in ['POINT'] else None
    crossover_size = population_size - elite_size
    if crossover_strategy_type == 'POINT':
        crossover_strategy = CrossoverStrategyEnum[crossover_strategy_type].value(intersection_number, crossover_size,
                                                                                  crossover_probability)
    else:
        crossover_strategy = CrossoverStrategyEnum[crossover_strategy_type].value(crossover_size,
                                                                                  crossover_probability)

    mutation_strategy_type = 'TWO_POINT'
    mutation_probability = config['mutation_prob']
    mutation_strategy = MutationStrategyEnum[mutation_strategy_type].value(mutation_probability)

    inversion = None
    is_inversion = config['inversion_prob'] is not None
    if is_inversion:
        inversion_probability = config['inversion_prob']
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
    start = time.time()
    evolution.evolve()
    end = time.time()

    best_ind = min(evolution.individuals, key=lambda x: function(x.decode_chromosomes_representation()))

    rep = best_ind.decode_chromosomes_representation() if best_ind else None
    app.popup(end - start, function(rep), rep)


app = Application()
app.button_start.configure(command=start_algorithm)
app.start()
