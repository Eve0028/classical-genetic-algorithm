from source.mutation.mutation import Mutation
from source.population.individual import Individual
import random

class OnePointMutation(Mutation):
    def mutate(self, individuals: list[Individual]) -> list[Individual]:
        for individual in individuals:
            for chromosome in individual.chromosomes:
                if random.random() <= self.mutation_probability:
                    gene = random.randint(0, len(chromosome) - 1)
                    chromosome[gene] = abs(1 - chromosome[gene])

        return individuals