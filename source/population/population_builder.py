from source.population.population import Population
from source.selection.selection_strategy import SelectionStrategy


class PopulationBuilder:
    def __init__(self):
        self.population_size = 0
        self.number_of_chromosomes = 0
        self.precision = 0
        self.start_interval = 0.0
        self.end_interval = 0.0
        self.selection_strategy = None
        self.fitness_function = None
        self.selection_size = None
        self.selection_percentage = 50.

    def set_population_size(self, size: int):
        self.population_size = size
        return self

    def set_number_of_chromosomes(self, number: int):
        self.number_of_chromosomes = number
        return self

    def set_precision(self, precision: int):
        self.precision = precision
        return self

    def set_intervals(self, start: float, end: float):
        self.start_interval = start
        self.end_interval = end
        return self

    def set_selection_strategy(self, strategy: SelectionStrategy):
        self.selection_strategy = strategy
        return self

    def set_fitness_function(self, fitness_function):
        self.fitness_function = fitness_function
        return self

    def set_selection_size(self, size: int):
        self.selection_size = size
        return self

    def set_selection_percentage(self, percentage: float):
        self.selection_percentage = percentage
        return self

    def build(self) -> Population:
        return Population(self.population_size, self.number_of_chromosomes, self.precision, self.start_interval,
                          self.end_interval, self.selection_strategy, self.fitness_function, self.selection_size,
                          self.selection_percentage)
