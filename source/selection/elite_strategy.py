import copy

from source.population.individual import Individual


def apply_elite_strategy(individuals: list[Individual], elite_size: int) -> list[Individual]:
    """
    Applies the elite strategy to select the top individuals.

    :param individuals: List of individuals in the population.
    :param elite_size: Number of top individuals to select.
    :return: List of top individuals. Returns a copy of the list.
    """
    sorted_individuals = sorted(individuals, key=lambda ind: ind.fitness, reverse=True)
    return copy.deepcopy(sorted_individuals[:elite_size])
