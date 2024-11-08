from source.genetic_algorithm.selection.roulette_selection import RouletteSelection
from source.genetic_algorithm.population.individual import Individual
from tests.selection.utils import calc_individuals_fitness


def test_roulette_selection_one_chromosome():
    individuals = [Individual(1, 10, 0, 1, generate=True) for _ in range(10)]
    fitness_function = lambda x: x
    calc_individuals_fitness(individuals, fitness_function, True)
    selection_strategy = RouletteSelection(selection_size=5)
    selected_individuals = selection_strategy.select(individuals)

    assert len(selected_individuals) == 5
    assert all(isinstance(ind, Individual) for ind in selected_individuals)


def test_roulette_selection_multiple_chromosomes():
    individuals = [Individual(3, 10, 0, 1, generate=True) for _ in range(10)]
    fitness_function = lambda x: sum(x)
    calc_individuals_fitness(individuals, fitness_function, True)
    selection_strategy = RouletteSelection(selection_size=5)
    selected_individuals = selection_strategy.select(individuals)

    assert len(selected_individuals) == 5
    assert all(isinstance(ind, Individual) for ind in selected_individuals)
