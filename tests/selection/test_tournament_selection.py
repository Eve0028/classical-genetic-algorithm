import pytest
from source.selection.tournament_selection import TournamentSelection
from source.population.individual import Individual


def test_tournament_selection_one_chromosome():
    individuals = [Individual(1, 10, 0, 1, generate=True) for _ in range(15)]
    fitness_function = lambda x: x
    selection_strategy = TournamentSelection()
    selected_individuals = selection_strategy.select(individuals, fitness_function, tournament_size=5)

    assert len(selected_individuals) == 3
    assert all(isinstance(ind, Individual) for ind in selected_individuals)


def test_tournament_selection_multiple_chromosomes():
    individuals = [Individual(3, 10, 0, 1, generate=True) for _ in range(12)]
    fitness_function = lambda x: sum(x)
    selection_strategy = TournamentSelection()
    selected_individuals = selection_strategy.select(individuals, fitness_function, tournament_size=3)

    assert len(selected_individuals) == 4
    assert all(isinstance(ind, Individual) for ind in selected_individuals)
