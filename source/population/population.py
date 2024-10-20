from source.population.individual import Individual
from source.utils.binary_utils import BinaryUtils


class Population:
    def __init__(self, population_size,  number_of_chromosomes, precision, start_interval, end_interval):
        self.population_size = population_size
        self.individuals = self.generate_individuals(population_size,  number_of_chromosomes, precision, start_interval,
                                                     end_interval)

    def generate_individuals(self, population_size, number_of_chromosomes, precision, start_interval, end_interval):
        number_of_genes = BinaryUtils.get_binary_length(start_interval, end_interval, precision)
        individuals = [Individual(number_of_chromosomes, number_of_genes, start_interval, end_interval) for _ in
                       range(population_size)]
        for individual in individuals:
            individual.generate_chromosomes()
        return individuals
