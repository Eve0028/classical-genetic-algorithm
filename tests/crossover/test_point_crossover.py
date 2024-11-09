from source.genetic_algorithm.population.individual import Individual
import numpy as np
from source.genetic_algorithm.crossover.point_crossover import PointCrossover


def test_cross_genes_when_two_point_crossover():
    expected_individual1_before = np.array([[0, 1, 0, 0, 0, 1, 0, 0, 0, 1]])
    expected_individual2_before = np.array([[1, 0, 1, 1, 1, 1, 1, 1, 1, 1]])
    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes = expected_individual1_before.copy()
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes = expected_individual2_before.copy()

    point_crossover = PointCrossover( 2, 0)
    point_crossover.cross_genes(0, individual1, individual2, 2, 5)

    expected_individual1_after = np.array([[0, 1, 1, 1, 1, 1, 0, 0, 0, 1]])
    expected_individual2_after = np.array([[1, 0, 0, 0, 0, 1, 1, 1, 1, 1]])

    np.testing.assert_array_equal(individual1.chromosomes, expected_individual1_after)
    np.testing.assert_array_equal(individual2.chromosomes, expected_individual2_after)


def test_cross_genes_when_one_point_crossover():
    expected_individual1_before = np.array([[0, 1, 0, 0, 0, 1, 0, 0, 0, 1]])
    expected_individual2_before = np.array([[1, 0, 1, 1, 1, 1, 1, 1, 1, 1]])
    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes = expected_individual1_before.copy()
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes = expected_individual2_before.copy()

    point_crossover = PointCrossover( 1, 0)
    point_crossover.cross_genes(0, individual1, individual2, 6, 9)

    expected_individual1_after = np.array([[0, 1, 0, 0, 0, 1, 1, 1, 1, 1]])
    expected_individual2_after = np.array([[1, 0, 1, 1, 1, 1, 0, 0, 0, 1]])

    np.testing.assert_array_equal(individual1.chromosomes, expected_individual1_after)
    np.testing.assert_array_equal(individual2.chromosomes, expected_individual2_after)


def test_cross_individuals_when_two_points_intersection_and_two_individuals():
    expected_individual1_before = np.array([[0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                                            [1, 1, 1, 0, 0, 1, 0, 0, 1, 1],
                                            [0, 0, 0, 1, 1, 0, 0, 1, 0, 0]])

    expected_individual2_before = np.array([[1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                                            [0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
                                            [1, 1, 1, 0, 0, 1, 1, 0, 1, 1]])
    individual1 = Individual(0, 0, 0, 0, False)
    individual1.number_of_chromosomes = 3
    individual1.chromosomes = expected_individual1_before.copy()
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes = expected_individual2_before.copy()
    individual2.number_of_chromosomes = 3

    point_crossover = PointCrossover( 2, 2)
    population = point_crossover.cross( [individual1, individual2])

    assert not np.array_equal(individual1.chromosomes, expected_individual1_before)
    assert not np.array_equal(individual2.chromosomes, expected_individual2_before)
    assert len(population) == 2


def test_cross_individuals_when_one_point_intersection_and_two_individuals():
    expected_individual1_before = np.array([[0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                                            [1, 1, 1, 0, 0, 1, 0, 0, 1, 1],
                                            [0, 0, 0, 1, 1, 0, 0, 1, 0, 0]])

    expected_individual2_before = np.array([[1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                                            [0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
                                            [1, 1, 1, 0, 0, 1, 1, 0, 1, 1]])
    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes = expected_individual1_before.copy()
    individual1.number_of_chromosomes = 3
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes = expected_individual2_before.copy()
    individual2.number_of_chromosomes = 3

    point_crossover = PointCrossover(1, 2)
    population = point_crossover.cross([individual1, individual2])

    assert not np.array_equal([individual1.chromosomes, individual2.chromosomes], [expected_individual1_before,expected_individual2_before])
    assert len(population) == 2


def test_cross_individuals_when_two_points_intersection_and_four_individuals():
    expected_individual1_before = np.array([[0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                                            [1, 1, 1, 0, 0, 1, 0, 0, 1, 1],
                                            [0, 0, 0, 1, 1, 0, 0, 1, 0, 0]])

    expected_individual2_before = np.array([[1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                                            [0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
                                            [1, 1, 1, 0, 0, 1, 1, 0, 1, 1]])

    expected_individual3_before = np.array([[1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
                                            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                                            [0, 1, 1, 1, 0, 1, 1, 1, 1, 0]])

    expected_individual4_before = np.array([[0, 0, 1, 0, 0, 1, 1, 0, 1, 1],
                                            [1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
                                            [1, 0, 1, 1, 1, 0, 0, 1, 0, 1]])

    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes = expected_individual1_before.copy()
    individual1.number_of_chromosomes = 3

    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes = expected_individual2_before.copy()
    individual2.number_of_chromosomes = 3

    individual3 = Individual(0, 0, 0, 0, False)
    individual3.chromosomes = expected_individual3_before.copy()
    individual3.number_of_chromosomes = 3

    individual4 = Individual(0, 0, 0, 0, False)
    individual4.chromosomes = expected_individual4_before.copy()
    individual4.number_of_chromosomes = 3

    point_crossover = PointCrossover(2, 4)
    population = point_crossover.cross([individual1, individual2, individual3, individual4])

    assert not np.array_equal([individual1.chromosomes, individual2.chromosomes, individual3.chromosomes, individual4.chromosomes],
                              [expected_individual1_before,expected_individual2_before])

    assert len(population) == 4, "Population should contain 4 individuals."
