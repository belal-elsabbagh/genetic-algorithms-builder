"""This module contains the GeneticAlgorithm class."""
import random
from typing import Callable

from src.ga.Individual import Individual


class GeneticAlgorithm(object):
    """Genetic Algorithm class."""

    __validate: Callable[[any], bool] = None
    __fitness: Callable[[Individual], float] = None
    __crossover: Callable[[list[Individual]], list[Individual]] = None
    __mutate: Callable[[Individual], Individual] = None
    __select: Callable[[list[Individual]], list[Individual]] = None

    def __init__(self, **kwargs):
        """Initialize the Genetic Algorithm class."""
        self.__validate = kwargs.get('validate')
        self.__fitness = kwargs.get('fitness')
        self.__crossover = kwargs.get('crossover')
        self.__mutate = kwargs.get('mutate')
        self.__select = kwargs.get('select')

    def run(self, population: list[Individual], generations, target, log: bool = True):
        pool = population
        """Run the Genetic Algorithm."""
        for gen_i in range(generations):
            pool = sorted(pool, key=lambda x: self.__fitness(x, target))
            if self.__fitness(pool[0], target) <= 0:
                return pool[0]
            pool = self.__reproduce(
                pool[:int(len(pool)*0.5)]) + self.__reproduce(
                pool[:int(len(pool)*0.5)]) + self.__select(pool)
            if log:
                print(self.__gen_log_msg(
                    gen_i, pool[0], self.__fitness(pool[0], target)))
        return pool

    def __reproduce(self, parents: list[Individual]):
        """Create a new generation of individuals."""
        new_gen = [
            self.__crossover(
                random.choice(parents),
                random.choice(parents)
            )
            for _ in range(len(parents))
        ]
        return [self.__mutate(ind) for ind in new_gen]

    def __gen_log_msg(self, generation, best: Individual, fitness_score):
        """Generate a log message."""
        return f'Gen {generation}:\tBest: {best.get_chromosome()}\tFitness: {fitness_score}'
