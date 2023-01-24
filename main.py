"""Main module for the genetic algorithm project."""

import random
import string
from typing import Callable
from src.ga import GeneticAlgorithmFactory
from src.ga.Individual import Individual
from src.ga.crossover import mate
from src.ga.fitness import match_target


CHARACTERS = string.ascii_lowercase + ' '


if __name__ == '__main__':
    target = "hello world"
    ga = GeneticAlgorithmFactory().create(
        fitness=match_target,
        crossover=mate,
        mutate=lambda x: x.add_mutations(CHARACTERS),
    )
    population = Individual.random_population(100, len(target), CHARACTERS)
    res = ga.run(population, 200, target, log=True)
    print(f"Answer: {res[0].get_chromosome()}")
