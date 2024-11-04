import numpy as np

from source.mutation.one_point_mutation import OnePointMutation
from source.population.individual import Individual

def get_starting_population(chromosomes : int, genes : int) -> list[Individual]:
    individuals = [Individual(chromosomes, genes, 0, 1) for _ in range(10)]
    for i in individuals:
        i.chromosomes = np.zeros((chromosomes,genes), dtype=int)
    return individuals

def test_one_point_mutation_one_chromosome_max_probability():
    individuals = get_starting_population(1, 10)

    mutation_strategy = OnePointMutation(1.0)
    mutated_individuals = mutation_strategy.mutate(individuals)

    count = 0
    for i in mutated_individuals:
        if any(i.chromosomes[0]) == 1:
            count += 1

    assert count == len(individuals)

def test_best_selection_multiple_chromosomes_max_probability():
    individuals = get_starting_population(3, 10)

    mutation_strategy = OnePointMutation(1.0)
    mutated_individuals = mutation_strategy.mutate(individuals)

    count = 0
    for i in mutated_individuals:
        for j in i.chromosomes:
            if any(j) == 1:
                count += 1

    assert count == len(individuals) * 3