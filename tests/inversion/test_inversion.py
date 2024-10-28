import numpy as np

from source.inversion.inversion import Inversion
from source.population.individual import Individual

def get_starting_population(chromosomes : int, genes : int) -> list[Individual]:
    individuals = [Individual(chromosomes, genes, 0, 1) for _ in range(10)]
    for i in individuals:
        i.chromosomes = np.zeros((chromosomes,genes), dtype=int)
    return individuals


def test_inversion_one_chromosome_max_probability():
    individuals = get_starting_population(1, 100)
    inversion_strategy = Inversion()

    inverted_individuals = inversion_strategy.inverse(individuals, 1.0)

    for individual in inverted_individuals:
        for chromosome in individual.chromosomes:
            assert np.count_nonzero(chromosome == 1) >= 2

def test_inversion_many_chromosomes_max_probability():
    individuals = get_starting_population(3, 100)
    inversion_strategy = Inversion()

    inverted_individuals = inversion_strategy.inverse(individuals, 1.0)

    for individual in inverted_individuals:
        assert np.count_nonzero(individual.chromosomes == 1) >= 6