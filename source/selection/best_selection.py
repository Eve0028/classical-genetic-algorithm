from typing import override

from source.selection.elite_strategy import apply_elite_strategy
from source.selection.selection_strategy import SelectionStrategy
from source.population.individual import Individual


class BestSelection(SelectionStrategy):
    @override
    def select(self, individuals: list[Individual], fitness_function, **kwargs) -> list[
        Individual]:
        """
        Selects the top individuals based on their fitness.

        :param individuals: List of individuals in the population.
        :param fitness_function: Fitness function to evaluate individuals.
        :keyword selection_size: Number of returned individuals.
        :return: List of top individuals.
        :raises ValueError: If selection_size is not specified.
        """
        selection_size = kwargs.get('selection_size')
        if selection_size is None:
            raise ValueError("Selection size must be specified.")
        return apply_elite_strategy(individuals, selection_size, fitness_function)
