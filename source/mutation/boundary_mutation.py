from source.mutation.mutation import Mutation
from source.population.individual import Individual
import random

class BoundaryMutation(Mutation):
    def mutate(self, individuals: list[Individual], mutation_probablity : float) -> list[Individual]:
        for individual in individuals:
            for chromosome in individual.chromosomes:
                if random.random() <= mutation_probablity:
                    chromosome[0] = abs(1 - chromosome[0])
                    chromosome[-1] = abs(1 - chromosome[-1])

        return individuals