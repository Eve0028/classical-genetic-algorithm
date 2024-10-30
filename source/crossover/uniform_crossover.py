from source.crossover.crossover import Crossover
from source.population.individual import Individual
import numpy as np
from typing import List
import copy

class UniformCrossover(Crossover):

    def __init__(self, crossover_probability=0.8):
        self.crossover_probability = crossover_probability

    def cross(self, population: List[Individual]) -> list[Individual]:
        if len(population) % 2 != 0:
            self.cross_individuals(copy.deepcopy(population[len(population) - 2]), population[len(population) - 1])

        for i in range(0, len(population) - 1, 2):
            self.cross_individuals(population[i], population[i + 1])
        return population

    def cross_individuals(self, individual1: Individual, individual2: Individual):
        for chromosome1, chromosome2 in zip(individual1.chromosomes, individual2.chromosomes):
            self.cross_genes(chromosome1, chromosome2)

    def cross_genes(self, chromosome1, chromosome2):
        for gene_index in range(len(chromosome1)):
            not_crossover = np.random.rand()
            if self.crossover_probability < not_crossover:
                continue
            chromosome1[gene_index], chromosome2[gene_index] = chromosome2[gene_index], chromosome1[gene_index]

