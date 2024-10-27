from source.mutation.mutation import Mutation
from source.population.individual import Individual
import random

class BoundaryMutation(Mutation):
    def mutate(self, individuals: list[Individual], mutation_probablity : float) -> list[Individual]:
        mutated_individuals = individuals.copy()
        for ind in mutated_individuals:
            if random.random() <= mutation_probablity:
                chromosomes_count = len(ind.chromosomes)
                i = random.randint(0, chromosomes_count - 1)
                ind.chromosomes[i][0] = abs(1 - ind.chromosomes[i][0])
                ind.chromosomes[i][-1] = abs(1 - ind.chromosomes[i][-1])

        return mutated_individuals