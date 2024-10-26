from typing import List
from source.population.individual import Individual
from abc import ABC, abstractmethod

class Crossover(ABC):

    @abstractmethod
    def cross(self, population: List[Individual]) -> list[Individual]:
        pass
