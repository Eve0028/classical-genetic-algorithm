from source.crossover.uniform_crossover import UniformCrossover
from source.population.individual import Individual
import numpy as np

def test_uniform_crossover1():
    uniform_crossover = UniformCrossover()
    uniform_crossover.crossover_probability=1
    expected_individual1_before = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    expected_individual2_before = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes= expected_individual1_before.copy()
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes= expected_individual2_before.copy()

    population = uniform_crossover.cross([individual1, individual2])

    np.testing.assert_array_equal(population[0].chromosomes,  expected_individual2_before)
    np.testing.assert_array_equal(population[1].chromosomes, expected_individual1_before)
    assert len(population) == 2

def test_uniform_crossover2():
    uniform_crossover = UniformCrossover()
    uniform_crossover.crossover_probability=1
    expected_individual1_before = np.array([[0, 1, 0, 1, 1, 0, 1, 0, 1, 0]])
    expected_individual2_before = np.array([[0, 0, 1, 1, 0, 1, 0, 1, 0, 0]])
    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes= expected_individual1_before.copy()
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes= expected_individual2_before.copy()

    population = uniform_crossover.cross([individual1, individual2])

    np.testing.assert_array_equal(population[0].chromosomes,  np.array([[1, 0, 1, 0, 0, 1, 0, 1, 0, 1]]))
    np.testing.assert_array_equal(population[1].chromosomes, np.array([[1, 1, 0, 0, 1, 0, 1, 0, 1, 1]]))