from source.evolution.evolution import Evolution
from source.evolution.functions import SimpleFunctionEnum
from source.evolution.strategies import SelectionStrategyEnum, CrossoverStrategyEnum, MutationStrategyEnum
from source.inversion.inversion import Inversion
from source.population.population import Population

population_size = 100
num_generations = 1000

function_name = 'HYPERSPHERE'
num_variables = 3
function = SimpleFunctionEnum[function_name].value[0](num_variables)
search_minimum = True
precision = 4
start_interval = SimpleFunctionEnum[function_name].value[1]
end_interval = SimpleFunctionEnum[function_name].value[2]

selection_strategy_type = 'TOURNAMENT'
selection_size = 50 if selection_strategy_type != 'TOURNAMENT' else None
tournament_size = 4 if selection_strategy_type == 'TOURNAMENT' else None
selection_strategy = SelectionStrategyEnum[selection_strategy_type].value(
    selection_size if selection_size else tournament_size)

# elite_strategy = True
elite_size = 3

crossover_strategy_type = 'UNIFORM'
crossover_probability = 0.8
intersection_number = 2 if crossover_strategy_type in ['POINT'] else None
crossover_size = population_size - elite_size
if crossover_strategy_type == 'POINT':
    crossover_strategy = CrossoverStrategyEnum[crossover_strategy_type].value(intersection_number, crossover_size,
                                                                              crossover_probability)
else:
    crossover_strategy = CrossoverStrategyEnum[crossover_strategy_type].value(crossover_size,
                                                                              crossover_probability)

mutation_strategy_type = 'TWO_POINT'
mutation_probability = 0.2
mutation_strategy = MutationStrategyEnum[mutation_strategy_type].value(mutation_probability)

inversion = None
is_inversion = True
if is_inversion:
    inversion_probability = 0.1
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
print(function(best_ind.decode_chromosomes_representation()))

print("Best individual: ", best_ind.chromosomes if best_ind else None)
print("Best ind values: ", best_ind.decode_chromosomes_representation() if best_ind else None)
