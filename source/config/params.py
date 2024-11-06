# For searching the hyperparameters
SIMPLE_FUNCTION_NAMES = ['ROSENBROCK']
# SIMPLE_FUNCTION_NAMES = ['SCHWEFEL', 'RASTRIGIN', 'ROSENBROCK']
NUM_VARIABLES = [2, 10, 30]
PRECISIONS = [4, 6, 8]

DB_PREFIX = "sqlite:///"
SIMPLE_DB_FILE = "simple_functions.db"
COMPLEX_DB_FILE = "complex_functions.db"
ACTUAL_DB_FILE_FULLNAME = f"{DB_PREFIX}{SIMPLE_DB_FILE}"
LOG_FILE = "evolution.log"
