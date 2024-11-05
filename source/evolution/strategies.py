from enum import Enum

from source.crossover.discrete_crossover import DiscreteCrossover
from source.crossover.point_crossover import PointCrossover
from source.crossover.uniform_crossover import UniformCrossover
from source.mutation.boundary_mutation import BoundaryMutation
from source.mutation.one_point_mutation import OnePointMutation
from source.mutation.two_point_mutation import TwoPointMutation
from source.selection.best_selection import BestSelection
from source.selection.roulette_selection import RouletteSelection
from source.selection.tournament_selection import TournamentSelection


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
