from typing import List

from source.genetic_algorithm.selection.selection_strategy import SelectionStrategy
from source.genetic_algorithm.population.individual import Individual


class BestSelection(SelectionStrategy):
    def __init__(self, selection_size: int):
        """
        Initializes the best selection strategy with the specified selection size.
        :param selection_size: Number of returned individuals.
        """
        self.selection_size = selection_size

    def select(self, individuals: List[Individual]) -> List[
        Individual]:
        """
        Selects the top individuals based on their fitness.

        :param individuals: List of individuals in the population.
        :return: List of top individuals.
        """
        sorted_individuals = sorted(individuals, key=lambda ind: ind.fitness, reverse=True)
        return sorted_individuals[:self.selection_size]
