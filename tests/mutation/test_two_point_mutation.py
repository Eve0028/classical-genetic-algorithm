import numpy as np
from source.mutation.two_point_mutation import TwoPointMutation
from source.population.individual import Individual

def get_starting_population(chromosomes : int, genes : int) -> list[Individual]:
    individuals = [Individual(chromosomes, genes, 0, 1) for _ in range(10)]
    for i in individuals:
        i.chromosomes = np.zeros((chromosomes,genes), dtype=int)
    return individuals

def test_two_point_mutation_one_chromosome_max_probability():
    individuals = get_starting_population(1, 10)

    mutation_strategy = TwoPointMutation(1.0)
    mutated_individuals = mutation_strategy.mutate(individuals)

    count = 0
    for i in mutated_individuals:
        count += sum(i.chromosomes[0])

    assert count == 2 * len(individuals)

def test_best_selection_multiple_chromosomes_max_probability():
    individuals = get_starting_population(3, 10)

    mutation_strategy = TwoPointMutation(1.0)
    mutated_individuals = mutation_strategy.mutate(individuals)

    count = 0
    for i in mutated_individuals:
        for j in i.chromosomes:
            count += sum(j)

    assert count == len(individuals) * 3 * 2