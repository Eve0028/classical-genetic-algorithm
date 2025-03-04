from collections.abc import Callable
from typing import List
import logging

from numpy import ndarray
import numpy as np

from source.config.logging_config import get_logger
from source.genetic_algorithm.population.individual import Individual
from source.genetic_algorithm.crossover.crossover import Crossover
from source.genetic_algorithm.mutation.mutation import Mutation
from source.genetic_algorithm.inversion.inversion import Inversion
from source.genetic_algorithm.selection.elite_strategy import apply_elite_strategy
from source.genetic_algorithm.selection.selection_strategy import SelectionStrategy

logger = get_logger()


class Evolution:
    def __init__(self, individuals: List[Individual], number_of_generations: int,
                 fitness_function: Callable,
                 search_minimum: bool,
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
            logger.error("elitism_size must be between 0 and the population size")
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

    def evaluate_fitness(self) -> ndarray:
        fitness_values = np.empty(0)
        for individual in self.individuals:
            fitness_value = self.fitness_function(individual.decode_chromosomes_representation())
            individual.fitness = 1 / fitness_value if self.search_minimum else fitness_value
            fitness_values = np.append(fitness_values, fitness_value)
        return fitness_values

    def select(self) -> None:
        self.individuals = self.selection_strategy.select(self.individuals)

    def crossover(self) -> None:
        self.individuals = self.crossover_strategy.cross(self.individuals)

    def mutation(self) -> None:
        self.individuals = self.mutation_strategy.mutate(self.individuals)

    def evolve(self) -> ndarray:
        """
        Evolves the population for the given number of generations.
        """
        after_selection_more_than_population_size = False
        fitness_values = np.empty((self.number_of_generations, self.population_size))
        for _ in range(self.number_of_generations):
            generation_fitness_values = self.evaluate_fitness()
            fitness_values[_] = generation_fitness_values.reshape(1, -1)

            if self.elitism_size:
                self.elite = apply_elite_strategy(self.individuals, self.elitism_size)

            self.select()
            # selection size should be checked when creating the selection strategy
            if (len(self.individuals) + self.elitism_size) > self.population_size:
                if not after_selection_more_than_population_size:
                    logger.warning("The selection strategy returned more individuals than the population size.")
                    after_selection_more_than_population_size = True

            self.crossover()
            # crossover size should be checked when creating the crossover strategy
            if (len(self.individuals) + self.elitism_size) > self.population_size:
                logger.error("The crossover strategy returned more individuals than the population size.")
                raise ValueError("The crossover strategy returned more individuals than the population size.")

            self.mutation()
            if self.inversion:
                self.individuals = self.inversion.inverse(self.individuals)

            if self.elitism_size:
                self.individuals.extend(self.elite)

            if len(self.individuals) != self.population_size:
                logger.error("The population size changed during evolution.")
                raise ValueError("The population size changed during evolution.")

        return fitness_values
