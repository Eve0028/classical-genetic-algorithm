import pytest
import numpy as np

from source.population.individual import Individual


def test_decode_chromosome_representation():
    individual = Individual(1, 25, -10, 10)
    individual.chromosomes = np.array([[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]])
    decoded_chromosome = individual.decode_chromosomes_representation()
    assert decoded_chromosome[0] == -4.824477279915729

    individual2 = Individual(2, 25, -10, 10)
    individual2.chromosomes = np.array([[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0],
                                        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]])
    decoded_chromosome2 = individual2.decode_chromosomes_representation()
    assert decoded_chromosome2[0] == -4.824477279915729
    assert decoded_chromosome2[1] == -4.824477279915729

    individual3 = Individual(3, 25, -10, 10)
    individual3.chromosomes = np.array([[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0],
                                        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0],
                                        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]])
    decoded_chromosome3 = individual3.decode_chromosomes_representation()
    assert decoded_chromosome3[0] == -4.824477279915729
    assert decoded_chromosome3[1] == -4.824477279915729
    assert decoded_chromosome3[2] == -4.824477279915729


def test_generate_chromosome():
    individual = Individual(5, 10, -10, 10)
    individual.generate_chromosomes()
    chromosome = individual.chromosomes
    assert chromosome.shape == (5, 10)
