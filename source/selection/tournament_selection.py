import random
from source.selection.selection_strategy import SelectionStrategy
from source.population.individual import Individual


class TournamentSelection(SelectionStrategy):
    def select(self, individuals: list[Individual], fitness_function, selection_size: int, tournament_size: int = 3,
               **kwargs) -> list[Individual]:
        """
        Selects individuals using tournament selection.

        :param individuals: List of individuals in the population.
        :param fitness_function: Fitness function to evaluate individuals.
        :param selection_size: Number of individuals to select.
        :param tournament_size: Number of individuals in each tournament.
        :return: List of selected individuals.
        """
        selected_individuals = []
        for _ in range(selection_size):
            tournament = random.sample(individuals, tournament_size)
            winner = max(tournament, key=lambda ind: ind.count_fitness_function(fitness_function))
            selected_individuals.append(winner)

        return selected_individuals
