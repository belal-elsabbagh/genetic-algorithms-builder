"""
Genetic Algorithm Factory class.
"""

from typing import Callable
from src.ga.GeneticAlgorithm import GeneticAlgorithm
from src.ga.Individual import Individual


class GeneticAlgorithmFactory(object):
    """Factory class for Genetic Algorithm objects."""

    def __init__(self):
        """Initialize the factory class."""
        pass

    def create(
        self,
        validate: callable = None,
        fitness: Callable[[Individual, any], float] = None,
        crossover=None,
        mutate=None,
        select=None
    ) -> GeneticAlgorithm:
        """Create a Genetic Algorithm object."""
        attributes = self.build_attributes(
            validate, fitness, crossover, mutate, select)
        return GeneticAlgorithm(
            validate=attributes['validate'],
            fitness=attributes['fitness'],
            crossover=attributes['crossover'],
            mutate=attributes['mutate'],
            select=attributes['select']
        )

    def build_attributes(
        self,
        validate: callable,
        fitness: Callable[[Individual, any], float],
        crossover,
        mutate,
        select
    ):
        """Initialize the default attributes."""
        return {
            'validate': validate if validate is not None else lambda x: True,
            'fitness': fitness if fitness is not None else lambda x, y: 0,
            'crossover': crossover if crossover is not None else lambda x, y: x,
            'mutate': mutate if mutate is not None else lambda x: x,
            'select': select if select is not None else lambda x: x[:int(len(x)*0.1)]
        }
