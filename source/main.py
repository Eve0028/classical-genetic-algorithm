from source.evolution.evolution import Evolution
from source.evolution.functions import SimpleFunctionEnum, ComplexFunctionEnum
from source.evolution.strategies import SelectionStrategyEnum, CrossoverStrategyEnum, MutationStrategyEnum
from source.gui.application import Application
from source.graph.graph import GraphCreator
from source.inversion.inversion import Inversion
from source.population.population import Population
from typing import Tuple
import numpy as np
import time
from threading import Thread


def get_configuration() -> Evolution:
    config = app.get_algorithm_config()
    population_size = config['population_size']
    num_generations = config['generations']
    num_variables = config['number_of_variables']
    precision = config['bits_count']
    search_minimum = config['search_minimum']
    start_interval = config['start_interval']
    end_interval = config['end_interval']

    function_name = config['function_name']
    if function_name == 'ROSENBROCK':
        function = SimpleFunctionEnum[function_name].value[0](num_variables)
    else:
        function = ComplexFunctionEnum[function_name].value[0](num_variables)

    selection_strategy_type = config['selection_strategy']
    selection_size = config['individuals_best'] if selection_strategy_type != 'TOURNAMENT' else None
    tournament_size = config['individuals_best'] if selection_strategy_type == 'TOURNAMENT' else None
    selection_strategy = SelectionStrategyEnum[selection_strategy_type].value(
        selection_size if selection_size else tournament_size)

    elite_strategy = config['individuals_elite'] is not None
    elite_size = config['individuals_elite'] if elite_strategy else 0

    crossover_strategy_type = config['cross_strategy']
    crossover_probability = config['cross_prob']
    intersection_number = config['intersection_number'] if crossover_strategy_type in ['POINT'] else None
    crossover_size = population_size - elite_size
    if crossover_strategy_type == 'POINT':
        crossover_strategy = CrossoverStrategyEnum[crossover_strategy_type].value(intersection_number, crossover_size,
                                                                                  crossover_probability)
    else:
        crossover_strategy = CrossoverStrategyEnum[crossover_strategy_type].value(crossover_size,
                                                                                  crossover_probability)

    mutation_strategy_type = config['mutation_strategy']
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
    return evolution


def start_algorithm(evolution: Evolution) -> Tuple[float, np.ndarray, float]:
    start = time.time()
    fitness_values = evolution.evolve()
    end = time.time()
    graph_creator = GraphCreator()
    graph_creator.create_graphs(fitness_values, evolution.search_minimum)

    best_ind = min(evolution.individuals,
                   key=lambda x: evolution.fitness_function(x.decode_chromosomes_representation()))
    rep = best_ind.decode_chromosomes_representation() if best_ind else None
    return end - start, rep, evolution.fitness_function(rep)


def start_submit_thread():
    global submit_thread
    app.button_start.configure(state="disabled")
    evolution = get_configuration()
    submit_thread = Thread(target=submit_, args=(evolution,))
    submit_thread.start()
    app.root.after(1000, check_submit_thread)


def submit_(evolution: Evolution):
    global exec_time, xs, ys
    exec_time, xs, ys = start_algorithm(evolution)
    return [exec_time, ys, xs]


def check_submit_thread():
    app.root.update_idletasks()
    if submit_thread and not submit_thread.is_alive():
        app.button_start.configure(state='normal')
        app.popup(exec_time, ys, xs)
    else:
        app.root.after(1000, check_submit_thread)


app = Application()
app.button_start.configure(command=start_submit_thread)
app.start()
