from enum import Enum
import benchmark_functions as bf

from source.evolution.happycat import ShiftedRotatedHappyCat


class SimpleFunctionEnum(Enum):
    SCHWEFEL = (bf.Schwefel, -500, 500)
    HYPERSPHERE = (bf.Hypersphere, -5, 5)
    HYPERELLIPSOID = (bf.Hyperellipsoid, -65.536, 65.536)
    RASTRIGIN = (bf.Rastrigin, -5.12, 5.12)
    ROSENBROCK = (bf.Rosenbrock, -2.048, 2.048)


class ComplexFunctionEnum(Enum):
    HAPPYCAT = (ShiftedRotatedHappyCat, -100, 100)
