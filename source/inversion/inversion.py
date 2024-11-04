from source.population.individual import Individual
import random

class Inversion:
    def __init__(self, inversion_probability : float = 0.2) -> None:
        self.inversion_probability = inversion_probability

    def inverse(self, individuals: list[Individual]) -> list[Individual]:
        """
        Inverse individual's genes.

        :param individuals: List of individuals in the population.
        :return: List of modified individuals.
        """
        for individual in individuals:
            for chromosome in individual.chromosomes:
                if random.random() <= self.inversion_probability:
                    start = random.randint(0, len(chromosome) - 1)
                    end = random.randint(0, len(chromosome) - 1)
                    while start == end:
                        end = random.randint(0, len(chromosome) - 1)

                    if start > end:
                        start, end = end, start

                    chromosome[start : end + 1] = chromosome[start : end + 1][::-1]

        return individuals