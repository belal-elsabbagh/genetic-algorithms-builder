"""Main module for the genetic algorithm project."""

import random
import string
from typing import Callable
from src.ga import GeneticAlgorithmFactory
from src.ga.Individual import Individual


CHARACTERS = string.ascii_lowercase + ' '


def cal_fitness(individual, target):
    '''
    Calculate fitness score, it is the number of
    characters in string which differ from target
    string.
    '''
    fitness = 0
    for gs, gt in zip(individual.get_chromosome(), target):
        if gs != gt:
            fitness += 1
    return fitness


def mate(par1: Individual, par2: Individual):
    '''
    Perform mating and produce new offspring
    '''
    child_chromosome = []
    for gp1, gp2 in zip(par1.get_chromosome(), par2.get_chromosome()):
        prob = random.random()
        if prob < 0.45:
            child_chromosome.append(gp1)
        elif prob < 0.90:
            child_chromosome.append(gp2)
        else:
            child_chromosome.append(random.choice(CHARACTERS))
    return Individual(child_chromosome)


def rand_individual():
    '''
    Create random individuals for mutation
    '''
    return Individual([random.choice(CHARACTERS) for _ in range(len("hello world"))])


if __name__ == '__main__':
    factory = GeneticAlgorithmFactory()
    ga = factory.create(
        fitness=cal_fitness,
        crossover=mate,
    )
    res = ga.run(Individual.create_random_population(
        100, rand_individual), 200, "hello world")
    print(f"Answer: {res.get_chromosome()}")
