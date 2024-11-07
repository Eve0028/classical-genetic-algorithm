WIDTH : int = 500
HEIGHT : int = 700

ENTRY_WIDTH : int = int(WIDTH / 10)
BUTTON_WIDTH : int = ENTRY_WIDTH - 5

BG_COLOR : str = "#191919"
FG_COLOR : str = "#FFFFFF"
HL_COLOR : str = "#017300"
BLACK : str = "#000000"
GREY : str = "#808080"
HL_BG_COLOR : str = "#0000C5"

FONT = lambda size: ("Arial", size)
LABEL_FONT_SIZE : int = 13

ENTRY_PADY: int = 5
ENTRY_PADX: int = 5
LABEL_PADY: int = 5

SELECTION_STRATEGY = ["Selection strategy: BEST", "Selection strategy: ROULETTE", "Selection strategy: TOURNAMENT"]
CROSS_STRATEGY = ["Cross strategy: POINT", "Cross strategy: DISCRETE", "Cross strategy: UNIFORM"]
MUTATION_STRATEGY = ["Mutation strategy: ONE_POINT", "Mutation strategy: TWO_POINT", "Mutation strategy: BOUNDARY"]
STRATEGY = lambda x : x.split(':')[1].strip()

FUNCTIONS_LIST = ['Function: ROSENBROCK', 'Function: HAPPYCAT']
FUNC = lambda x : x.split(':')[1].strip()
VALIDATE = lambda x : x if x > 0 else None

DEFAULTS = {
    "Interval start (a)" : "-2.048",
    "Interval end (b)" : "2.048",
    "Population size" : "286",
    "Number of variables" : "3",
    "Bits per chromosome (precision)" : "3",
    "Number of generations" : "586",
    "Number of individuals (best / tournament)" : "2",
    "Number of individuals (elite)" : "22",
    "Number of intersections (point crossover)" : "1",
    "Cross probability" : "0.711",
    "Mutation probability" : "0.064",
    "Inversion probability" : "0.285"
}