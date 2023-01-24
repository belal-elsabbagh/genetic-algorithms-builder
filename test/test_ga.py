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
        return EUROPE_GRAPH.keys().get(start).get(end, 10000)

    def get_cost_of_path(path):
        return sum([get_cost_of_edge(previous, current) for previous, current in zip(path, path[1:])])

    if ind.get_chromosome()[0] != target[0]:
        return 10000

    return get_cost_of_path(ind.get_chromosome())


def crossover(ind1, ind2):
    prob = random.random()
    child_chromosome = []
    if prob < 0.45:
        child_chromosome = ind1.get_chromosome()
        child_chromosome.append(ind2.get_chromosome()[-1])
    elif prob < 0.90:
        child_chromosome = ind2.get_chromosome()
        child_chromosome.append(ind1.get_chromosome()[-1])
    else:
        child_chromosome.append(None)
    return Individual(child_chromosome)


def mutate(ind):
    new_ind = ind.add_mutations(list(EUROPE_GRAPH.keys()))
    new_ind.get_chromosome().append(random.choice(list(EUROPE_GRAPH.keys())))
    return new_ind


def test_shortest_path():
    """Test the genetic algorithm with a given target function."""
    target = ('Arad', 'Bucharest')
    ga = GeneticAlgorithmFactory().create(
        fitness=path_cost,
        crossover=mate,
        mutate=mutate,
    )
    population = Individual.random_population(
        100, 1, ['Arad'] + list(EUROPE_GRAPH.keys()))
    res = ga.run(population, 2000, target, log=True)
    assert res[0].get_chromosome()[0] == target[0]
    assert res[0].get_chromosome()[-1] == target[1]
