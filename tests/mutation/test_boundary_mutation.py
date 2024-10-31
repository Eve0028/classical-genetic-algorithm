import numpy as np

from source.mutation.boundary_mutation import BoundaryMutation
from source.population.individual import Individual

def get_starting_population(chromosomes : int, genes : int) -> list[Individual]:
    individuals = [Individual(chromosomes, genes, 0, 1) for _ in range(10)]
    for i in individuals:
        i.chromosomes = np.zeros((chromosomes,genes), dtype=int)
    return individuals

def test_boundary_mutation_one_chromosome_max_probability():
    individuals = get_starting_population(1, 10)

    mutation_strategy = BoundaryMutation(1.0)
    mutated_individuals = mutation_strategy.mutate(individuals)

    assert all(individual.chromosomes[0][0] == 1 for individual in mutated_individuals)
    assert all(individual.chromosomes[0][-1] == 1 for individual in mutated_individuals)


def test_boundary_mutation_many_chromosome_max_probability():
    individuals = get_starting_population(3, 10)

    mutation_strategy = BoundaryMutation(1.0)
    mutated_individuals = mutation_strategy.mutate(individuals)

    assert all(chromosome[0] == 1 for individual in mutated_individuals for chromosome in individual.chromosomes)
    assert all(chromosome[-1] == 1 for individual in mutated_individuals for chromosome in individual.chromosomes)