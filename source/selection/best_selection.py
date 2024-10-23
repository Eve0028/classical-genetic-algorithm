from source.selection.elite_strategy import apply_elite_strategy
from source.selection.selection_strategy import SelectionStrategy
from source.population.individual import Individual


class BestSelection(SelectionStrategy):
    def select(self, individuals: list[Individual], fitness_function, selection_size: int, **kwargs) -> list[
        Individual]:
        """
        Selects the top individuals based on their fitness.

        :param individuals: List of individuals in the population.
        :param fitness_function: Fitness function to evaluate individuals.
        :param selection_size: Number of top individuals to select.
        :return: List of top individuals.
        """
        return apply_elite_strategy(individuals, selection_size, fitness_function)
