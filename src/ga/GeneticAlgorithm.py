"""This module contains the GeneticAlgorithm class."""
import random
from typing import Callable

from src.ga.Individual import Individual


class GeneticAlgorithm(object):
    """Genetic Algorithm class."""

    _fitness: Callable[[Individual], float] = None
    _crossover: Callable[[list[Individual]], list[Individual]] = None
    _mutate: Callable[[Individual], Individual] = None
    _select: Callable[[list[Individual]], list[Individual]] = None

    def __init__(self, **kwargs):
        """Initialize the Genetic Algorithm class."""
        self._fitness = kwargs.get('fitness')
        self._crossover = kwargs.get('crossover')
        self._mutate = kwargs.get('mutate')
        self._select = kwargs.get('select')
        
    def get_fitness(self):
        return self._fitness
    
    def get_crossover(self):
        return self._crossover
    
    def get_mutate(self):
        return self._mutate
    
    def get_select(self):
        return self._select

    def run(self, population: list[Individual], generations, log: bool = False, reverse: bool = False):
        pool = population
        """Run the Genetic Algorithm."""
        for gen_i in range(generations):
            pool = sorted(pool, key=lambda x: self._fitness(x), reverse=reverse)
            best_individual = pool[0]
            best_fitness = self._fitness(best_individual)
            if log:
                print(self._log_msg(gen_i, best_individual, best_fitness) + f'\tPool: {len(pool)}')
            if best_fitness <= 0:
                return pool
            pool = self._new_pool(pool)
        return pool

    def _reproduce(self, parents: list[Individual]):
        """Create a new generation of individuals."""
        new_gen = [
            self._crossover(
                random.choice(parents),
                random.choice(parents),
            )
            for _ in range(len(parents*2))
        ]
        return [self._mutate(ind) for ind in new_gen]

    def _log_msg(self, generation, best: Individual, fitness_score):
        """Generate a log message."""
        return f'Gen {generation}:\tBest: {"".join(best.get_chromosome())}\tFitness: {fitness_score}'

    @staticmethod
    def _get_ratio(population: list[Individual], ratio: float):
        """Return the fittest individual in the population."""
        return population[:int(len(population)*ratio)]

    def _new_pool(self, pool: list[Individual]):
        """Create a new pool of individuals."""
        return self._reproduce(self._get_ratio(pool, 0.5)) + self._select(pool)


class NumberGeneticAlgorithm(GeneticAlgorithm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
