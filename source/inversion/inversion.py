from source.population.individual import Individual
import random

class Inversion:
    @staticmethod
    def inverse(individuals: list[Individual], inversion_probablity : float) -> list[Individual]:
        """
        Inverse individual's genes.

        :param individuals: List of individuals in the population.
        :param inversion_probablity: Probability of inversion.
        :return: List of modified individuals.
        """
        for individual in individuals:
            for chromosome in individual.chromosomes:
                if random.random() <= inversion_probablity:
                    start = random.randint(0, len(chromosome) - 1)
                    end = random.randint(0, len(chromosome) - 1)
                    while start == end:
                        end = random.randint(0, len(chromosome) - 1)

                    if start > end:
                        start, end = end, start

                    for gene in range(start, end + 1):
                        chromosome[gene] = abs(1 - chromosome[gene])

        return individuals