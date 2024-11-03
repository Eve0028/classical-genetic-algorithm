from source.crossover.uniform_crossover import UniformCrossover
from source.population.individual import Individual
import numpy as np

def test_uniform_crossover1():
    uniform_crossover = UniformCrossover(2)
    uniform_crossover.crossover_probability=1
    expected_individual1_before = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    expected_individual2_before = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes= expected_individual1_before.copy()
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes= expected_individual2_before.copy()

    uniform_crossover.cross_individuals(individual1, individual2)

    np.testing.assert_array_equal(individual1.chromosomes,  expected_individual2_before)
    np.testing.assert_array_equal(individual2.chromosomes, expected_individual1_before)


def test_uniform_crossover3():
    uniform_crossover = UniformCrossover(2)
    uniform_crossover.crossover_probability=1
    expected_individual1_before = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    expected_individual2_before = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes= expected_individual1_before.copy()
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes= expected_individual2_before.copy()

    uniform_crossover.cross_individuals(individual1, individual2)

    np.testing.assert_array_equal(individual1.chromosomes,  expected_individual2_before)
    np.testing.assert_array_equal(individual2.chromosomes, expected_individual1_before)

def test_uniform_crossover4():
    uniform_crossover = UniformCrossover(2)
    uniform_crossover.crossover_probability=1
    expected_individual1_before = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    expected_individual2_before = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes= expected_individual1_before.copy()
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes= expected_individual2_before.copy()

    population = uniform_crossover.cross_individuals(individual1, individual2)

    np.testing.assert_array_equal(individual1.chromosomes,  expected_individual2_before)
    np.testing.assert_array_equal(individual2.chromosomes, expected_individual1_before)

def test_uniform_crossover5():
    uniform_crossover = UniformCrossover(4)
    uniform_crossover.crossover_probability=1
    expected_individual1_before = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    expected_individual2_before = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes= expected_individual1_before.copy()
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes= expected_individual2_before.copy()

    expected_individual3_before = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    expected_individual4_before = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    individual3 = Individual(0, 0, 0, 0, False)
    individual3.chromosomes= expected_individual3_before.copy()
    individual4 = Individual(0, 0, 0, 0, False)
    individual4.chromosomes= expected_individual4_before.copy()

    population = uniform_crossover.cross([individual1, individual2, individual3, individual4])

    assert len(population) == 4
    not np.array_equal(
        [individual1.chromosomes, individual2.chromosomes, individual3.chromosomes, individual4.chromosomes],
        [population[0].chromosomes, population[1].chromosomes, population[2].chromosomes, population[3].chromosomes])

def test_uniform_crossover_when_crossover_should_not_happen():
    uniform_crossover = UniformCrossover(2)
    uniform_crossover.crossover_probability=0
    expected_individual1_before = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    expected_individual2_before = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes= expected_individual1_before.copy()
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes= expected_individual2_before.copy()

    population = uniform_crossover.cross_individuals(individual1, individual2)

    np.testing.assert_array_equal(individual1.chromosomes,  expected_individual1_before)
    np.testing.assert_array_equal(individual2.chromosomes, expected_individual2_before)

def test_uniform_crossover2():
    uniform_crossover = UniformCrossover(2)
    uniform_crossover.crossover_probability=1
    expected_individual1_before = np.array([[0, 1, 0, 1, 1, 0, 1, 0, 1, 0]])
    expected_individual2_before = np.array([[0, 0, 1, 1, 0, 1, 0, 1, 0, 0]])
    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes= expected_individual1_before.copy()
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes= expected_individual2_before.copy()

    population = uniform_crossover.cross_individuals(individual1, individual2)

    np.testing.assert_array_equal(individual1.chromosomes,  np.array([[0, 0, 1, 1, 0, 1, 0, 1, 0, 0]]))
    np.testing.assert_array_equal(individual2.chromosomes, np.array([[0, 1, 0, 1, 1, 0, 1, 0, 1, 0]]))


def test_uniform_crossover6():
    uniform_crossover = UniformCrossover(3)
    uniform_crossover.crossover_probability=1
    expected_individual1_before = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    expected_individual2_before = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    expected_individual3_before = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

    expected_individual4_before = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes= expected_individual1_before.copy()
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes= expected_individual2_before.copy()
    individual3 = Individual(0, 0, 0, 0, False)
    individual3.chromosomes= expected_individual3_before.copy()
    individual4 = Individual(0, 0, 0, 0, False)
    individual4.chromosomes = expected_individual4_before.copy()

    population = uniform_crossover.cross([individual1, individual2, individual3, individual4])

    assert len(population) == 3