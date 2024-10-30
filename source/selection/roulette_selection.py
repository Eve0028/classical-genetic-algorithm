import random
import bisect
from typing import override

from source.selection.selection_strategy import SelectionStrategy
from source.population.individual import Individual


class RouletteSelection(SelectionStrategy):
    @override
    def select(self, individuals: list[Individual], fitness_function, **kwargs) -> list[
        Individual]:
        """
        Selects individuals based on their fitness using roulette wheel selection.

        :param individuals: List of individuals in the population.
        :param fitness_function: Fitness function to evaluate individuals.
            For the minimization problem, the passed fitness function is already inverted.
        :keyword selection_size: Number of returned individuals.
        :return: List of selected individuals.
        :raises ValueError: If selection_size is not specified.
        """
        selection_size = kwargs.get('selection_size')
        if selection_size is None:
            raise ValueError("Selection size must be specified.")

        # Calculate the fitness values for each individual and the total sum of the fitnesses
        fitness_values = [ind.count_fitness_function(fitness_function) for ind in individuals]
        total_fitness = sum(fitness_values)

        # Normalization and calculation of the distribution
        cumulative_distribution = []
        cumulative_sum = 0
        for fitness in fitness_values:
            cumulative_sum += fitness / total_fitness
            cumulative_distribution.append(cumulative_sum)

        # Selection of individuals using distribution and binary search (bisect_left - czas O(log(n)))
        selected_individuals = []
        for _ in range(selection_size):
            pick = random.uniform(0, 1)
            index = bisect.bisect_left(cumulative_distribution, pick)  # Find the right index in the distribution
            selected_individuals.append(individuals[index])

        return selected_individuals
