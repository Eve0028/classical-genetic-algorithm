import pytest
from source.selection.roulette_selection import RouletteSelection
from source.population.individual import Individual


def test_roulette_selection_one_chromosome():
    individuals = [Individual(1, 10, 0, 1, generate=True) for _ in range(10)]
    fitness_function = lambda x: x
    selection_strategy = RouletteSelection()
    selected_individuals = selection_strategy.select(individuals, fitness_function, selection_size=5)

    assert len(selected_individuals) == 5
    assert all(isinstance(ind, Individual) for ind in selected_individuals)


import pytest
from source.selection.roulette_selection import RouletteSelection
from source.population.individual import Individual


def test_roulette_selection_multiple_chromosomes():
    individuals = [Individual(3, 10, 0, 1, generate=True) for _ in range(10)]
    fitness_function = lambda x: sum(x)
    selection_strategy = RouletteSelection()
    selected_individuals = selection_strategy.select(individuals, fitness_function, selection_size=5)

    assert len(selected_individuals) == 5
    assert all(isinstance(ind, Individual) for ind in selected_individuals)
