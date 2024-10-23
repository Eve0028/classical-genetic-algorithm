import pytest
from source.population.population_builder import PopulationBuilder
from source.selection.best_selection import BestSelection
from source.population.individual import Individual


def test_population_builder_basic():
    builder = PopulationBuilder()
    population = (builder.set_population_size(10)
                  .set_number_of_chromosomes(2)
                  .set_precision(5)
                  .set_intervals(0.0, 1.0)
                  .set_selection_strategy(BestSelection())
                  .set_fitness_function(lambda x: sum(x))
                  .build())

    assert population.population_size == 10
    assert population.number_of_chromosomes == 2
    assert population.precision == 5
    assert population.start_interval == 0.0
    assert population.end_interval == 1.0
    assert isinstance(population.selection_strategy, BestSelection)
    assert callable(population.fitness_function)
    assert len(population.individuals) == 10
    assert all(isinstance(ind, Individual) for ind in population.individuals)


def test_population_builder_with_selection_size():
    builder = PopulationBuilder()
    population = (builder.set_population_size(10)
                  .set_number_of_chromosomes(2)
                  .set_precision(5)
                  .set_intervals(0.0, 1.0)
                  .set_selection_strategy(BestSelection())
                  .set_fitness_function(lambda x: sum(x))
                  .set_selection_size(5)
                  .build())

    assert population.selection_size == 5


def test_population_builder_with_selection_percentage():
    builder = PopulationBuilder()
    population = (builder.set_population_size(10)
                  .set_number_of_chromosomes(2)
                  .set_precision(5)
                  .set_intervals(0.0, 1.0)
                  .set_selection_strategy(BestSelection())
                  .set_fitness_function(lambda x: sum(x))
                  .set_selection_percentage(50)
                  .build())

    assert population.selection_size == 5  # 50% z 10 to 5


def test_population_builder_with_invalid_selection_size():
    builder = PopulationBuilder()
    with pytest.raises(ValueError):
        builder.set_population_size(10) \
            .set_number_of_chromosomes(2) \
            .set_precision(5) \
            .set_intervals(0.0, 1.0) \
            .set_selection_strategy(BestSelection()) \
            .set_fitness_function(lambda x: sum(x)) \
            .set_selection_size(15) \
            .build()
