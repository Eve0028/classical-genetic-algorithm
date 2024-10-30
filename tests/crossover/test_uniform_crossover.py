from source.crossover.uniform_crossover import UniformCrossover
from source.population.individual import Individual
import numpy as np

def test_uniform_crossover1():
    uniform_crossover = UniformCrossover()
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

    population = uniform_crossover.cross([individual1, individual2])

    np.testing.assert_array_equal(population[0].chromosomes,  expected_individual2_before)
    np.testing.assert_array_equal(population[1].chromosomes, expected_individual1_before)
    assert len(population) == 2

def test_uniform_crossover3():
    uniform_crossover = UniformCrossover()
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

    population = uniform_crossover.cross([individual1, individual2])

    np.testing.assert_array_equal(population[0].chromosomes,  expected_individual2_before)
    np.testing.assert_array_equal(population[1].chromosomes, expected_individual1_before)
    assert len(population) == 2

def test_uniform_crossover4():
    uniform_crossover = UniformCrossover()
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

    population = uniform_crossover.cross([individual1, individual2])

    np.testing.assert_array_equal(population[0].chromosomes,  expected_individual2_before)
    np.testing.assert_array_equal(population[1].chromosomes, expected_individual1_before)
    assert len(population) == 2

def test_uniform_crossover5():
    uniform_crossover = UniformCrossover()
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

    np.testing.assert_array_equal(population[0].chromosomes,  expected_individual2_before)
    np.testing.assert_array_equal(population[1].chromosomes, expected_individual1_before)
    np.testing.assert_array_equal(population[2].chromosomes,  expected_individual4_before)
    np.testing.assert_array_equal(population[3].chromosomes, expected_individual3_before)
    assert len(population) == 4


def test_uniform_crossover_when_crossover_should_not_happen():
    uniform_crossover = UniformCrossover()
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

    population = uniform_crossover.cross([individual1, individual2])

    np.testing.assert_array_equal(population[0].chromosomes,  expected_individual1_before)
    np.testing.assert_array_equal(population[1].chromosomes, expected_individual2_before)
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

    np.testing.assert_array_equal(population[0].chromosomes,  np.array([[0, 0, 1, 1, 0, 1, 0, 1, 0, 0]]))
    np.testing.assert_array_equal(population[1].chromosomes, np.array([[0, 1, 0, 1, 1, 0, 1, 0, 1, 0]]))


def test_uniform_crossover6():
    uniform_crossover = UniformCrossover()
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
    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes= expected_individual1_before.copy()
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes= expected_individual2_before.copy()
    individual3 = Individual(0, 0, 0, 0, False)
    individual3.chromosomes= expected_individual3_before.copy()

    population = uniform_crossover.cross([individual1, individual2, individual3])

    np.testing.assert_array_equal(population[0].chromosomes,  expected_individual2_before)
    np.testing.assert_array_equal(population[1].chromosomes, expected_individual1_before)
    np.testing.assert_array_equal(population[2].chromosomes, expected_individual2_before)
    assert len(population) == 3