from source.crossover.crossover import Crossover
from source.population.individual import Individual
import numpy as np
from typing import List

class UniformCrossover(Crossover):

    def __init__(self, crossover_probability=0.8):
        self.crossover_probability = crossover_probability

    def cross(self, population: List[Individual]) -> list[Individual]:
        for individual in population:
            for chromosome in individual.chromosomes :
                self.cross_genes(chromosome)

        return population

    def cross_genes(self, chromosome):
        for gene_index in range(len(chromosome)):
            not_crossover = np.random.rand()
            if self.crossover_probability < not_crossover:
                continue
            # XOR
            chromosome[gene_index] ^= 1