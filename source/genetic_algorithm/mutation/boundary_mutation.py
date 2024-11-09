from source.genetic_algorithm.mutation.mutation import Mutation
from source.genetic_algorithm.population.individual import Individual
import random

class BoundaryMutation(Mutation):
    def mutate(self, individuals: list[Individual]) -> list[Individual]:
        for individual in individuals:
            for chromosome in individual.chromosomes:
                if random.random() <= self.mutation_probability:
                    chromosome[0] = abs(1 - chromosome[0])
                    chromosome[-1] = abs(1 - chromosome[-1])

        return individuals