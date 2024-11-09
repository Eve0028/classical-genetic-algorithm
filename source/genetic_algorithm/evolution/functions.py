from enum import Enum
import benchmark_functions as bf

from opfunu.cec_based.cec2014 import F132014


class SimpleFunctionEnum(Enum):
    """
    Enumeration of simple benchmark functions.
    """
    SCHWEFEL = bf.Schwefel
    HYPERSPHERE = bf.Hypersphere
    HYPERELLIPSOID = bf.Hyperellipsoid
    RASTRIGIN = bf.Rastrigin
    ROSENBROCK = bf.Rosenbrock


class ComplexFunctionEnum(Enum):
    """
    Enumeration of complex benchmark functions.
    """
    HAPPYCAT = F132014
