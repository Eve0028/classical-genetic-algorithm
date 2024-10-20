import numpy as np

from source.utils.binary_utils import BinaryUtils


class Individual:

    def __init__(self, number_of_chromosomes, number_of_genes, start_interval, end_interval):
        self.number_of_chromosomes = number_of_chromosomes
        self.start_interval = start_interval
        self.end_interval = end_interval
        self.number_of_genes = number_of_genes
        self.chromosomes = []

    def generate_chromosomes(self):
        self.chromosomes = np.random.randint(0, 2, size=(self.number_of_chromosomes, self.number_of_genes))

    def decode_chromosomes_representation(self):
        return np.apply_along_axis(self.__decode_chromosome_representation, axis=1, arr=self.chromosomes)

    def __decode_chromosome_representation(self, chromosome):
        return self.start_interval + (BinaryUtils.decode_number(chromosome) * (self.end_interval - self.start_interval)) / (
                2 ** self.number_of_genes - 1)
