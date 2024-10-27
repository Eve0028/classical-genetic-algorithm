import random

from source.mutation.mutation import Mutation
from source.population.individual import Individual


class TwoPointMutation(Mutation):
    def mutate(self, individuals: list[Individual], mutation_probablity : float) -> list[Individual]:
        mutated_individuals = individuals.copy()
        for ind in mutated_individuals:
            if random.random() <= mutation_probablity:
                i = random.randint(0, len(ind.chromosomes) - 1)
                j = random.randint(0, len(ind.chromosomes[i]) - 1)
                k = random.randint(0, len(ind.chromosomes[i]) - 1)
                while k != j:
                    k = random.randint(0, len(ind.chromosomes[i]) - 1)

                ind.chromosomes[i][j] = abs(1 - ind.chromosomes[i][j])
                ind.chromosomes[i][k] = abs(1 - ind.chromosomes[i][k])

        return mutated_individuals