from abc import ABC
from typing import List
import logging

from source.genetic_algorithm.population.individual import Individual
from source.config.logging_config import get_logger

logger = get_logger()


class SelectionStrategy(ABC):
    def select(self, individuals: List[Individual]) -> List[Individual]:
        """
        Selects a subset of individuals based on the implemented selection strategy.

        :param individuals: The list of individuals to select from.
        :return: The selected subset of individuals.
        """
        pass

    @staticmethod
    def calculate_selection_size(individuals: List[Individual], selection_size: int = None,
                                 selection_percentage: float = 50.) -> int:
        # Calculate the selection size based on the provided parameters.
        # If both selection_size and selection_percentage are provided, selection_size is used.
        if selection_size is None and selection_percentage is None:
            logger.error("Either selection_size or selection_percentage must be provided.")
            raise ValueError("Either selection_size or selection_percentage must be provided.")

        if selection_size is not None:
            if selection_size > len(individuals):
                logger.error("Selection size cannot be greater than the number of individuals.")
                raise ValueError("Selection size cannot be greater than the number of individuals.")
            return selection_size

        if selection_percentage is not None:
            return int(len(individuals) * selection_percentage / 100)
