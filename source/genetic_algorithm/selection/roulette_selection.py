import random
import bisect

from source.genetic_algorithm.selection.selection_strategy import SelectionStrategy
from source.genetic_algorithm.population.individual import Individual


class RouletteSelection(SelectionStrategy):
    def __init__(self, selection_size: int):
        """
        Initializes the best selection strategy with the specified selection size.
        :param selection_size: Number of returned individuals.
        """
        self.selection_size = selection_size

    def select(self, individuals: list[Individual]) -> list[Individual]:
        """
        Selects individuals based on their fitness using roulette wheel selection.

        :param individuals: List of individuals in the population.
        :return: List of selected individuals.
        """

        # Calculate the total sum of the fitnesses
        fitness_values = [ind.fitness for ind in individuals]
        total_fitness = sum(fitness_values)

        # Normalization and calculation of the distribution
        cumulative_distribution = []
        cumulative_sum = 0
        for fitness in fitness_values:
            cumulative_sum += fitness / total_fitness
            cumulative_distribution.append(cumulative_sum)

        # Selection of individuals using distribution and binary search (bisect_left - time O(log(n)))
        selected_individuals = []
        for _ in range(self.selection_size):
            pick = random.uniform(0, 1)
            index = bisect.bisect_left(cumulative_distribution, pick)  # Find the right index in the distribution
            selected_individuals.append(individuals[index])

        return selected_individuals
