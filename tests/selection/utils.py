def calc_individuals_fitness(individuals, fitness_function, minimum) -> None:
    for individual in individuals:
        fitness_value = fitness_function(individual.decode_chromosomes_representation())
        individual.fitness = 1 / fitness_value if minimum else fitness_value
