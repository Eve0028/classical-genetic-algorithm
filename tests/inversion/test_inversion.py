import numpy as np

from source.genetic_algorithm.inversion.inversion import Inversion
from source.genetic_algorithm.population.individual import Individual

def get_starting_population(chromosomes : int, genes : int) -> list[Individual]:
    individuals = [Individual(chromosomes, genes, 0, 1, True) for _ in range(10)]
    return individuals

def test_inversion_max_probability():
    individuals = get_starting_population(3, 100)
    inversion_strategy = Inversion(1.0)

    ones = 0
    for i in individuals:
        ones += np.count_nonzero(chromosome == 1 for chromosome in i.chromosomes)

    inverted_individuals = inversion_strategy.inverse(individuals)
    ones_inverted = 0
    for i in inverted_individuals:
        ones_inverted += np.count_nonzero(chromosome == 1 for chromosome in i.chromosomes)

    assert ones == ones_inverted