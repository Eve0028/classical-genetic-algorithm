import random
from typing import override, List, Callable

from source.selection.selection_strategy import SelectionStrategy
from source.population.individual import Individual


class TournamentSelection(SelectionStrategy):
    @override
    def select(self, individuals: List[Individual], fitness_function: Callable,
               **kwargs) -> List[Individual]:
        """
        Selects individuals using tournament selection.

        :param individuals: List of individuals in the population.
        :param fitness_function: Fitness function to evaluate individuals.
        :param kwargs: Additional keyword arguments for selection strategies.
        :keyword tournament_size: Number of individuals in each tournament.
        :return: List of selected individuals.
        :raises ValueError: If tournament_size is not specified or is greater than the number of individuals.
        """
        tournament_size = kwargs.get('tournament_size')
        if tournament_size is None:
            raise ValueError("Tournament size must be specified.")
        if tournament_size > len(individuals):
            raise ValueError("Tournament size cannot be greater than the number of individuals.")

        selected_individuals = []
        random.shuffle(individuals)  # Shuffle individuals to ensure random grouping

        # Split individuals into groups of tournament_size
        groups = [individuals[i:i + tournament_size] for i in range(0, len(individuals), tournament_size)]

        # If the last group is smaller, we add it to the previous group
        if len(groups[-1]) < tournament_size and len(groups) > 1:
            groups[-2].extend(groups[-1])
            groups.pop()

        for group in groups:
            winner = max(group, key=lambda ind: ind.count_fitness_function(fitness_function))
            selected_individuals.append(winner)

        return selected_individuals
