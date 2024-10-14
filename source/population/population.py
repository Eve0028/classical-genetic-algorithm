from source.population.individual import Individual
from source.utils.binary_utils import BinaryUtils


class Population:
    def __init__(self, population_size, number_of_genes, precision, start_interval, end_interval):
        self.population_size = population_size
        self.individuals = self.generate_individuals(population_size, number_of_genes, precision, start_interval,
                                                     end_interval)

    def generate_individuals(self, population_size, number_of_genes, precision, start_interval, end_interval):
        binary_length = BinaryUtils.get_binary_length(start_interval, end_interval, precision)
        individuals = [Individual(number_of_genes, binary_length, start_interval, end_interval) for _ in
                       range(population_size)]
        for individual in individuals:
            individual.generate_chromosome()
        return individuals
