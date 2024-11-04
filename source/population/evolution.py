from collections.abc import Callable
from typing import List

from source.population.individual import Individual
from source.crossover.crossover import Crossover
from source.mutation.mutation import Mutation
from source.inversion.inversion import Inversion
from source.selection.elite_strategy import apply_elite_strategy
from source.selection.selection_strategy import SelectionStrategy


class Evolution:
    def __init__(self, individuals: List[Individual], number_of_generations: int, fitness_function: Callable, search_minimum: bool,
                 selection_strategy: SelectionStrategy,
                 crossover_strategy: Crossover,
                 mutation_strategy: Mutation,
                 inversion: Inversion = None,
                 elitism_size: int = 0):
        """
        Initializes an Evolution with the given parameters. Mutation

        :param individuals: Individuals of Population to evolve.
        :param number_of_generations: Number of generations to evolve.
        :param fitness_function: Function used to evaluate the fitness of individuals.
        :param selection_strategy: Strategy used for selection.
        :param crossover_strategy: Strategy used for crossover.
        :param mutation_strategy: Strategy used for mutation.
        :param inversion: Whether to use inversion.
        :param elitism_size: Number of top individuals to keep.
        """
        self.individuals = individuals
        self.population_size = len(self.individuals)
        if not (0 <= elitism_size <= self.population_size):
            raise ValueError("elitism_size must be between 0 and the population size")
        self.number_of_generations = number_of_generations
        self.fitness_function = fitness_function
        self.search_minimum = search_minimum
        self.selection_strategy = selection_strategy
        self.crossover_strategy = crossover_strategy
        self.mutation_strategy = mutation_strategy
        self.inversion = inversion
        self.elitism_size = elitism_size
        self.elite = None

    def evaluate_fitness(self) -> None:
        for individual in self.individuals:
            fitness_value = self.fitness_function(individual)
            individual.fitness = 1 / fitness_value if self.search_minimum else fitness_value

    def select(self) -> None:
        self.individuals = self.selection_strategy.select(self.individuals)

    def crossover(self) -> None:
        self.individuals = self.crossover_strategy.cross(self.individuals)

    def mutation(self) -> None:
        self.individuals = self.mutation_strategy.mutate(self.individuals)

    def evolve(self) -> None:
        """
        Evolves the population for the given number of generations.
        """
        for _ in range(self.number_of_generations):
            self.evaluate_fitness()

            if self.elitism_size:
                self.elite = apply_elite_strategy(self.individuals, self.elitism_size)

            self.select()
            # selection size should be checked when creating the selection strategy
            if len(self.individuals) + self.elitism_size > self.population_size:
                raise ValueError("The selection strategy returned more individuals than the population size.")

            self.crossover()
            # crossover size should be checked when creating the crossover strategy
            if len(self.individuals) + self.elitism_size > self.population_size:
                raise ValueError("The crossover strategy returned more individuals than the population size.")

            self.mutation()
            if inversion:
                self.individuals = inversion.inverse(self.individuals)

            if self.elitism_size:
                self.individuals.extend(self.elite)

            if len(self.individuals) != self.population_size:
                raise ValueError("The population size changed during evolution.")
