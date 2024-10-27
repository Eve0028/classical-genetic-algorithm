from source.population.individual import Individual
import random

class Inversion:
    @staticmethod
    def inverse(individuals: list[Individual], inversion_probablity : float) -> list[Individual]:
        """
        Inverse individual's genes.

        :param individuals: List of individuals in the population.
        :param inversion_probablity: Fitness function to evaluate individuals.
        :param inversion_probablity: Probability of inversion.
        :return: List of modified individuals.
        """
        inverted_individuals = individuals.copy()
        for ind in inverted_individuals:
            if random.random() <= inversion_probablity:
                i = random.randint(0, len(ind.chromosomes) - 1)
                j = random.randint(0, len(ind.chromosomes[i]) - 1)
                k = random.randint(0, len(ind.chromosomes[i]) - 1)
                while k != j:
                    k = random.randint(0, len(ind.chromosomes[i]) - 1)

                if k < j:
                    j, k = k, j

                for idx in range(j, k + 1):
                    ind.chromosomes[i][idx] = abs(1 - ind.chromosomes[i][idx])

        return inverted_individuals