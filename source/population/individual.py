import numpy as np

from source.utils.binary_utils import BinaryUtils


class Individual:

    def __init__(self, number_of_chromosomes: int, number_of_genes: int, start_interval: float, end_interval: float, generate: bool = True):
        """
        Initializes an Individual with the given parameters.

        :param start_interval: Start of the interval for gene values.
        :param end_interval: End of the interval for gene values.
        :param generate: Whether to generate chromosomes upon initialization.
        """
        self.number_of_chromosomes = number_of_chromosomes
        self.start_interval = start_interval
        self.end_interval = end_interval
        self.number_of_genes = number_of_genes
        self.chromosomes = []
        if generate:
            self.generate_chromosomes()
        self.fitness = None

    def generate_chromosomes(self) -> None:
        """
        Generates random chromosomes for the individual.
        Each chromosome is a binary array of genes.
        """
        self.chromosomes = np.random.randint(0, 2, size=(self.number_of_chromosomes, self.number_of_genes))

    def decode_chromosomes_representation(self) -> np.ndarray:
        """
        Decodes the binary representation of chromosomes to decimal values.
        """
        return np.apply_along_axis(self.__decode_chromosome_representation, axis=1, arr=self.chromosomes)

    def __decode_chromosome_representation(self, chromosome: np.ndarray) -> float:
        """
        Decodes a single chromosome from binary to decimal.

        :param chromosome: Binary representation of a chromosome.
        :return: Decimal value of the chromosome.
        """
        return self.start_interval + (BinaryUtils.decode_number(chromosome) * (self.end_interval - self.start_interval)) / (
                2 ** self.number_of_genes - 1)
