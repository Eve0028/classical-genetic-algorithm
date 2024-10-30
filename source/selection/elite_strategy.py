from source.population.individual import Individual


def apply_elite_strategy(individuals: list[Individual], elite_size: int, fitness_function) -> list[Individual]:
    """
    Applies the elite strategy to select the top individuals.

    :param individuals: List of individuals in the population.
    :param elite_size: Number of top individuals to select.
    :param fitness_function: Fitness function to evaluate individuals.
    :return: List of top individuals.
    """
    sorted_individuals = sorted(individuals,
                                    key=lambda ind: ind.count_fitness_function(fitness_function),
                                    reverse=True)
    return sorted_individuals[:elite_size]
