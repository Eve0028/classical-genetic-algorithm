from source.population.individual import Individual
from source.utils.binary_utils import BinaryUtils

from source.config.logging_config import logger


class Population:
    def __init__(self, population_size: int, number_of_chromosomes: int, precision: int,
                 start_interval: float, end_interval: float, generate: bool = True):
        """
        Initializes a Population with the given parameters.

        :param population_size: Number of individuals in the population.
        :param number_of_chromosomes: Number of chromosomes per individual.
        :param precision: Precision for gene values.
        :param start_interval: Start of the interval for gene values.
        :param end_interval: End of the interval for gene values.
        :param generate: Whether to generate individuals upon initialization.
        """
        if population_size <= 0:
            logger.error("population_size must be a positive integer.")
            raise ValueError("population_size must be a positive integer.")
        if number_of_chromosomes <= 0:
            logger.error("number_of_chromosomes must be a positive integer.")
            raise ValueError("number_of_chromosomes must be a positive integer.")
        if precision <= 0:
            logger.error("precision must be a positive integer.")
            raise ValueError("precision must be a positive integer.")
        if start_interval >= end_interval:
            logger.error("start_interval must be less than end_interval.")
            raise ValueError("start_interval must be less than end_interval.")

        self.population_size = population_size
        self.number_of_chromosomes = number_of_chromosomes
        self.precision = precision
        self.start_interval = start_interval
        self.end_interval = end_interval
        self.individuals = []
        if generate:
            self.individuals = self.generate_individuals()

    def generate_individuals(self) -> list:
        number_of_genes = BinaryUtils.get_binary_length(self.start_interval, self.end_interval, self.precision)
        return [Individual(self.number_of_chromosomes, number_of_genes, self.start_interval, self.end_interval,
                           generate=True) for _ in range(self.population_size)]
