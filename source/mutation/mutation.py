from abc import abstractmethod
from source.population.individual import Individual

class Mutation:
    @abstractmethod
    def mutate(self, individuals: list[Individual], mutation_probablity : float) -> list[Individual]:
        """
        Mutate individuals base on chosen Mutate strategy

        :param individuals: The list of individuals to select from.
        :param mutation_probablity: Probability of mutation.
        :return: List of mutated Individuals.
        """
        pass