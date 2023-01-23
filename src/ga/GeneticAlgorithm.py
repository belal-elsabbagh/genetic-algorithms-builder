"""This module contains the GeneticAlgorithm class."""
import random
from typing import Callable

from src.ga.Individual import Individual


class GeneticAlgorithm(object):
    """Genetic Algorithm class."""

    __fitness: Callable[[Individual], float] = None
    __crossover: Callable[[list[Individual]], list[Individual]] = None
    __mutate: Callable[[Individual], Individual] = None
    __select: Callable[[list[Individual]], list[Individual]] = None

    def __init__(self, **kwargs):
        """Initialize the Genetic Algorithm class."""
        self.__fitness = kwargs.get('fitness')
        self.__crossover = kwargs.get('crossover')
        self.__mutate = kwargs.get('mutate')
        self.__select = kwargs.get('select')

    def run(self, population: list[Individual], generations, target, log: bool = False):
        pool = population
        """Run the Genetic Algorithm."""
        for gen_i in range(generations):
            pool = sorted(pool, key=lambda x: self.__fitness(x, target))
            best_individual = pool[0]
            best_fitness = self.__fitness(best_individual, target)
            if log:
                print(self.__log_msg(gen_i, best_individual, best_fitness))
            if best_fitness <= 0:
                return pool
            pool = self.__new_pool(pool)
        return pool

    def __reproduce(self, parents: list[Individual]):
        """Create a new generation of individuals."""
        new_gen = [
            self.__crossover(
                random.choice(parents),
                random.choice(parents)
            )
            for _ in range(len(parents*2))
        ]
        return [self.__mutate(ind) for ind in new_gen]

    def __log_msg(self, generation, best: Individual, fitness_score):
        """Generate a log message."""
        return f'Gen {generation}:\tBest: {best.get_chromosome()}\tFitness: {fitness_score}'

    @staticmethod
    def __get_ratio(population: list[Individual], ratio: float):
        """Return the fittest individual in the population."""
        return population[:int(len(population)*ratio)]

    def __new_pool(self, pool: list[Individual]):
        """Create a new pool of individuals."""
        return self.__reproduce(self.__get_ratio(pool, 0.5)) + self.__select(pool)
