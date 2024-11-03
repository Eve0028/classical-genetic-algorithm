from typing import List

from source.crossover.crossover import Crossover
from source.population.individual import Individual
import numpy as np
from source.crossover.random_generator import RandomGenerator


class DiscreteCrossover(Crossover):

    def __init__(self, crossover_size: int, crossover_probability=0.5):
        super().__init__(crossover_size, crossover_probability)

    def cross(self, population: List[Individual]) -> list[Individual]:
        new_population = []
        chromosome_size = len(population[0].chromosomes)
        number_of_genes = len(population[0].chromosomes[0])
        i = self.crossover_size
        while i > 0:
            individual1, individual2 = self.generate_individuals(population)
            chromosomes = self.generate_chromosome(individual1, individual2, chromosome_size, number_of_genes)
            self.create_new_individual(individual1, chromosomes, new_population)
            i -= 1

        return new_population[:self.crossover_size]

    def generate_chromosome(self, individual1: Individual, individual2: Individual, chromosome_size: int,
                            number_of_genes: int) -> list[list[int]]:
        chromosomes = []
        for chromosome in range(0, chromosome_size):
            genes = []
            for gene in range(0, number_of_genes):
                new_gene = self.generate_gene(individual1, individual2, chromosome, gene)
                genes.append(new_gene)
            chromosomes.append(genes)
        return chromosomes

    def generate_gene(self, individual1: Individual, individual2: Individual, chromosome: int, gene: int) -> list[int]:
        probability = np.random.rand()
        if probability <= self.crossover_probability:
            return individual1.chromosomes[chromosome][gene]
        else:
            return individual2.chromosomes[chromosome][gene]

    def create_new_individual(self, individual1: Individual, chromosomes: list[list[int]],
                              new_population: List[Individual]):
        new_individual = individual1.copy()
        new_individual.chromosomes = chromosomes
        new_population.append(new_individual)
