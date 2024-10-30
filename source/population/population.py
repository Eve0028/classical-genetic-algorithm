from source.population.individual import Individual
from source.selection.selection_strategy import SelectionStrategy
from source.utils.binary_utils import BinaryUtils


class Population:
    def __init__(self, population_size: int, number_of_chromosomes: int, precision: int, start_interval: float,
                 end_interval: float, selection_strategy: SelectionStrategy, fitness_function,
                 selection_size: int = None,
                 selection_percentage: float = None, generate: bool = True):
        """
        Initializes a Population with the given parameters.

        :param population_size: Number of individuals in the population.
        :param number_of_chromosomes: Number of chromosomes per individual.
        :param precision: Precision for gene values.
        :param start_interval: Start of the interval for gene values.
        :param end_interval: End of the interval for gene values.
        :param selection_strategy: Strategy used for selection.
        :param fitness_function: Function used to evaluate the fitness of individuals.
        :param selection_size: Number of individuals to select.
        :param selection_percentage: Percentage of individuals to select.
        :param generate: Whether to generate individuals upon initialization.
        """
        self.population_size = population_size
        self.number_of_chromosomes = number_of_chromosomes
        self.precision = precision
        self.start_interval = start_interval
        self.end_interval = end_interval
        self.selection_strategy = selection_strategy
        self.fitness_function = fitness_function
        self.individuals = []
        if generate:
            self.individuals = self.generate_individuals()
        self.selection_size = self.selection_strategy.calculate_selection_size(self.individuals, selection_size,
                                                                               selection_percentage)

    def generate_individuals(self) -> list:
        number_of_genes = BinaryUtils.get_binary_length(self.start_interval, self.end_interval, self.precision)
        return [Individual(self.number_of_chromosomes, number_of_genes, self.start_interval, self.end_interval,
                           generate=True) for _ in range(self.population_size)]

    def select(self, **kwargs) -> list[Individual]:
        return self.selection_strategy.select(self.individuals, self.fitness_function)
