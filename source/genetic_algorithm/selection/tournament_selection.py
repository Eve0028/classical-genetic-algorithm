import random
from typing import List

from source.genetic_algorithm.selection.selection_strategy import SelectionStrategy
from source.genetic_algorithm.population.individual import Individual
from source.config.logging_config import get_logger

logger = get_logger()


class TournamentSelection(SelectionStrategy):
    def __init__(self, tournament_size: int = 3):
        """
        Initializes the tournament selection strategy with the specified tournament size.
        :param tournament_size: Number of individuals in each tournament.
        """
        self.tournament_size = tournament_size

    def select(self, individuals: List[Individual]) -> List[Individual]:
        """
        Selects individuals using tournament selection.

        :param individuals: List of individuals in the population.
        :return: List of selected individuals.
        :raises ValueError: If tournament_size is greater than the number of individuals.
        """
        if self.tournament_size > len(individuals):
            logger.error("Tournament size cannot be greater than the number of individuals.")
            raise ValueError("Tournament size cannot be greater than the number of individuals.")

        selected_individuals = []
        random.shuffle(individuals)  # Shuffle individuals to ensure random grouping

        # Split individuals into groups of tournament_size
        groups = [individuals[i:i + self.tournament_size] for i in range(0, len(individuals), self.tournament_size)]

        # If the last group is smaller, we add it to the previous group
        if len(groups[-1]) < self.tournament_size and len(groups) > 1:
            groups[-2].extend(groups[-1])
            groups.pop()

        for group in groups:
            winner = max(group, key=lambda ind: ind.fitness)
            selected_individuals.append(winner)

        return selected_individuals
