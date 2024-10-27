from source.mutation.mutation import Mutation
from source.population.individual import Individual
import random

class OnePointMutation(Mutation):
    def mutate(self, individuals: list[Individual], mutation_probablity : float) -> list[Individual]:
        mutated_individuals = individuals.copy()
        for ind in mutated_individuals:
            if random.random() <= mutation_probablity:
                chromosomes_count = len(ind.chromosomes)
                i = random.randint(0, chromosomes_count - 1)
                j = random.randint(0, len(ind.chromosomes[i]) - 1)
                ind.chromosomes[i][j] = abs(1 - ind.chromosomes[i][j])

        return mutated_individuals