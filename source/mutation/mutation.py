from abc import abstractmethod
from source.population.individual import Individual

class Mutation:
    def __init__(self, mutation_probability : float = 0.2) -> None:
        self.mutation_probability = mutation_probability

    @abstractmethod
    def mutate(self, individuals: list[Individual]) -> list[Individual]:
        """
        Mutate individuals base on chosen Mutate strategy

        :param individuals: The list of individuals to select from.
        :return: List of mutated Individuals.
        """
        pass