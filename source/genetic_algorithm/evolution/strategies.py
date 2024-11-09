from enum import Enum

from source.genetic_algorithm.crossover.discrete_crossover import DiscreteCrossover
from source.genetic_algorithm.crossover.point_crossover import PointCrossover
from source.genetic_algorithm.crossover.uniform_crossover import UniformCrossover
from source.genetic_algorithm.mutation.boundary_mutation import BoundaryMutation
from source.genetic_algorithm.mutation.one_point_mutation import OnePointMutation
from source.genetic_algorithm.mutation.two_point_mutation import TwoPointMutation
from source.genetic_algorithm.selection.best_selection import BestSelection
from source.genetic_algorithm.selection.roulette_selection import RouletteSelection
from source.genetic_algorithm.selection.tournament_selection import TournamentSelection


class SelectionStrategyEnum(Enum):
    BEST = BestSelection
    ROULETTE = RouletteSelection
    TOURNAMENT = TournamentSelection


class CrossoverStrategyEnum(Enum):
    POINT = PointCrossover
    DISCRETE = DiscreteCrossover
    UNIFORM = UniformCrossover


class MutationStrategyEnum(Enum):
    ONE_POINT = OnePointMutation
    TWO_POINT = TwoPointMutation
    BOUNDARY = BoundaryMutation
