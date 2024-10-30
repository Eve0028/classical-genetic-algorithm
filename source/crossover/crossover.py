from typing import List
from source.population.individual import Individual
from abc import ABC, abstractmethod

class Crossover(ABC):

    def __init__(self, crossover_probability):
        self.crossover_probability = crossover_probability

    @abstractmethod
    def cross(self, population: List[Individual]) -> list[Individual]:
        pass
