"""This module contains the GeneticAlgorithm class."""
from typing import Callable

from src.ga.Individual import Individual


class GeneticAlgorithm(object):
    """Genetic Algorithm class."""

    __encode: Callable = None
    __decode: Callable = None
    __validate: Callable[[any], bool] = None
    __fitness: Callable = None
    __crossover: Callable[[list[Individual]], list[Individual]] = None
    __mutate: Callable[[Individual], Individual] = None
    __select: Callable[[list[Individual]], list[Individual]] = None

    def __init__(self, **kwargs):
        """Initialize the Genetic Algorithm class."""
        self.__encode = kwargs.get('encode')
        self.__decode = kwargs.get('decode')
        self.__validate = kwargs.get('validate')
        self.__fitness = kwargs.get('fitness')
        self.__crossover = kwargs.get('crossover')
        self.__mutate = kwargs.get('mutate')
        self.__select = kwargs.get('select')

    def run(self, population, generations):
        """Run the Genetic Algorithm."""
        pool = population
        for _ in range(generations):
            parents = self.__select(pool)
            pool = self.__validate_individuals(self.__reproduce(parents))
        return pool

    def __validate_individuals(self, individuals):
        """Validate a list of individuals."""
        return [i for i in [self.__validate(i) for i in individuals]]

    def __reproduce(self, parents):
        """Create a new generation of individuals."""
        return [i for i in [self.__mutate(i) for i in self.__crossover(parents)]]
