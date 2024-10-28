from source.mutation.mutation import Mutation
from source.population.individual import Individual
import random

class OnePointMutation(Mutation):
    def mutate(self, individuals: list[Individual], mutation_probablity : float) -> list[Individual]:
        for individual in individuals:
            for chromosome in individual.chromosomes:
                if random.random() <= mutation_probablity:
                    gene = random.randint(0, len(chromosome) - 1)
                    chromosome[gene] = abs(1 - chromosome[gene])

        return individuals