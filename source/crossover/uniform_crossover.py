from source.crossover.crossover import Crossover
from source.population.individual import Individual
import numpy as np
from typing import List
import copy


class UniformCrossover(Crossover):

    def __init__(self, crossover_size: int, crossover_probability=0.8):
        super().__init__(crossover_size, crossover_probability)

    def cross(self, population: List[Individual]) -> list[Individual]:
        i = self.crossover_size
        new_population = []
        while i > 0:
            individual1, individual2 = self.generate_individuals(population)
            self.cross_individuals(individual1, individual2)
            new_population.append(individual1)
            new_population.append(individual2)
            i=i-2
        return new_population[:self.crossover_size]


    def cross_individuals(self, individual1: Individual, individual2: Individual):
        for chromosome1, chromosome2 in zip(individual1.chromosomes, individual2.chromosomes):
            self.cross_genes(chromosome1, chromosome2)

    def cross_genes(self, chromosome1, chromosome2):
        for gene_index in range(len(chromosome1)):
            not_crossover = np.random.rand()
            if self.crossover_probability < not_crossover:
                continue
            chromosome1[gene_index], chromosome2[gene_index] = chromosome2[gene_index], chromosome1[gene_index]
