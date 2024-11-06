from enum import Enum
import benchmark_functions as bf

from opfunu.cec_based.cec2014 import F132014


class SimpleFunctionEnum(Enum):
    """
    Enumeration of simple benchmark functions with their respective ranges.
    """
    SCHWEFEL = (bf.Schwefel, -500, 500)
    HYPERSPHERE = (bf.Hypersphere, -5, 5)
    HYPERELLIPSOID = (bf.Hyperellipsoid, -65.536, 65.536)
    RASTRIGIN = (bf.Rastrigin, -5.12, 5.12)
    ROSENBROCK = (bf.Rosenbrock, -2.048, 2.048)


class ComplexFunctionEnum(Enum):
    """
    Enumeration of complex benchmark functions with their respective ranges and variable counts.
    """
    HAPPYCAT = (F132014.evaluate, -100, 100, [10, 50, 100])
    # HAPPYCAT = (F132014.evaluate, -100, 100, [10, 20, 30, 50, 100])
