import random
from source.selection.selection_strategy import SelectionStrategy
from source.population.individual import Individual


class RouletteSelection(SelectionStrategy):
    def select(self, individuals: list[Individual], fitness_function, selection_size: int, **kwargs) -> list[
        Individual]:
        """
        Selects individuals based on their fitness using roulette wheel selection.

        :param individuals: List of individuals in the population.
        :param fitness_function: Fitness function to evaluate individuals.
        :param selection_size: Number of individuals to select.
        :return: List of selected individuals.
        """
        total_fitness = sum(ind.count_fitness_function(fitness_function) for ind in individuals)
        selected_individuals = []

        for _ in range(selection_size):
            pick = random.uniform(0, total_fitness)
            current = 0
            for individual in individuals:
                current += individual.count_fitness_function(fitness_function)
                if current > pick:
                    selected_individuals.append(individual)
                    break

        return selected_individuals
