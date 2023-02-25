"""
Test the genetic algorithm.
"""

import math
import string
from src.ga.Individual import Individual, NSpacePointIndividual, NumberIndividual
from src.util import match_target
from src.ga import NumberGeneticAlgorithm
from src.ga import TargetMatchingGeneticAlgorithm


CHARACTERS = string.ascii_lowercase + ' '


def test_target_string():
    """Test the genetic algorithm with a given target function."""
    target = "hello world"
    ga = TargetMatchingGeneticAlgorithm.create(
        fitness=match_target,
        crossover=Individual.mate,
        mutate=lambda x: x.add_mutations(CHARACTERS),
    )
    population = Individual.random_population(100, len(target), CHARACTERS)
    res = ga.run(population, 1000, target)
    assert res[0].get_chromosome() == list(target)


def test_numeric_algorithm():
    """Test the genetic algorithm with a numeric target function."""
    ga = NumberGeneticAlgorithm(
        fitness=lambda x: abs(25 - float(x)*float(x)),
        crossover=lambda x, y: x + y,
        mutate=NumberIndividual.mutate,
        select=lambda x: x[:int(len(x)*0.05)],
    )
    population = NumberIndividual.random_population(50, list(range(1025)))
    res = ga.run(population, 200)
    assert float(res[0]) == 5
