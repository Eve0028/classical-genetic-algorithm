from source.genetic_algorithm.population.population import Population


def test_generate_individuals():
    population = Population(5, 3, 6, -10, 10)
    assert len(population.individuals) == 5
    for i in range(5):
        assert len(population.individuals[i].chromosomes) == 3
        for j in range(3):
            assert len(population.individuals[i].chromosomes[j]) == 25
