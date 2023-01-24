"""
Test the genetic algorithm.
"""

import random
import string
from data.graph import EUROPE_GRAPH
from src.ga.Individual import Individual
from src.ga.crossover import mate
from src.ga.fitness import match_target
from src.ga.GeneticAlgorithmFactory import GeneticAlgorithmFactory


CHARACTERS = string.ascii_lowercase + ' '


def test_target_string():
    """Test the genetic algorithm with a given target function."""
    target = "hello world"
    ga = GeneticAlgorithmFactory().create(
        fitness=match_target,
        crossover=mate,
        mutate=lambda x: x.add_mutations(CHARACTERS),
    )
    population = Individual.random_population(100, len(target), CHARACTERS)
    res = ga.run(population, 200, target)
    assert res[0].get_chromosome() == list(target)


def path_cost(ind, target):
    def get_cost_of_edge(start, end):
        return EUROPE_GRAPH.get(start).get(end, 10000)

    def get_cost_of_path(path):
        return sum([get_cost_of_edge(previous, current) for previous, current in zip(path, path[1:])])

    if ind.get_chromosome()[0] != target[0]:
        return 10000

    return get_cost_of_path(ind.get_chromosome())


def test_shortest_path():
    """Test the genetic algorithm with a given target function."""
    target = ['Arad', 'Sibiu', 'RimnicuVilcea', 'Pitesti', 'Bucharest']
    ga = GeneticAlgorithmFactory().create(
        fitness=match_target,
        crossover=mate,
        mutate=lambda x: x.add_mutations(list(EUROPE_GRAPH.keys())),
    )
    population = Individual.random_population(
        100, len(target), list(EUROPE_GRAPH.keys()))
    res = ga.run(population, 2000, target, log=True)
    assert res[0].get_chromosome() == target
