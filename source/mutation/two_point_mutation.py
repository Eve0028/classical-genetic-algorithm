import random

from source.mutation.mutation import Mutation
from source.population.individual import Individual

class TwoPointMutation(Mutation):
    def mutate(self, individuals: list[Individual]) -> list[Individual]:
        for individual in individuals:
            for chromosome in individual.chromosomes:
                if random.random() <= self.mutation_probability:
                    first_gene = random.randint(0, len(chromosome) - 1)
                    second_gene = random.randint(0, len(chromosome) - 1)
                    while second_gene == first_gene:
                        second_gene = random.randint(0, len(chromosome) - 1)
                    chromosome[first_gene] = abs(1 - chromosome[first_gene])
                    chromosome[second_gene] = abs(1 - chromosome[second_gene])

        return individuals