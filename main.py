"""Main module for the genetic algorithm project."""

import string
from src.ga import GeneticAlgorithmFactory
from src.ga.TargetMatchingGeneticAlgorithm import TargetMatchingGeneticAlgorithm
from src.ga.Individual import Individual
from src.util import mate, match_target


CHARACTERS = string.ascii_lowercase + ' '


if __name__ == '__main__':
    target = "covenant of the deep"
    ga = GeneticAlgorithmFactory().create(
        fitness=match_target,
        crossover=mate,
        mutate=lambda x: x.add_mutations(CHARACTERS),
        ga_type=TargetMatchingGeneticAlgorithm
    )
    population = Individual.random_population(50, len(target), CHARACTERS)
    res = ga.run(population, 200, target, log=True)
    print(f"Answer: {res[0].get_chromosome()}")
