import numpy as np

from source.utils.binary_utils import BinaryUtils


class Individual:

    def __init__(self, number_of_genes, binary_length, start_interval, end_interval):
        self.number_of_genes = number_of_genes
        self.start_interval = start_interval
        self.end_interval = end_interval
        self.binary_length = binary_length
        self.chromosome = []

    def generate_chromosome(self):
        self.chromosome = np.random.randint(0, 2, size=(self.number_of_genes, self.binary_length))

    def decode_chromosome_representation(self):
        return np.apply_along_axis(self.__decode_gene_representation, axis=1, arr=self.chromosome)

    def __decode_gene_representation(self, gene):
        return self.start_interval + (BinaryUtils.decode_number(gene) * (self.end_interval - self.start_interval)) / (
                2 ** self.binary_length - 1)
