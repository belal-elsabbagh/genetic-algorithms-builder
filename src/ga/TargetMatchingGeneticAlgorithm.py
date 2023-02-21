"""This module contains the GeneticAlgorithm class."""
from src.ga.Individual import Individual
from src.ga.GeneticAlgorithm import GeneticAlgorithm

class TargetMatchingGeneticAlgorithm(GeneticAlgorithm):
    """Genetic Algorithm class with target matching."""

    def __init__(self, **kwargs):
        """Initialize the Genetic Algorithm class."""
        super().__init__(**kwargs)

    def run(self, population: list[Individual], generations, target, log: bool = False):
        pool = population
        """Run the Genetic Algorithm."""
        for gen_i in range(generations):
            pool = sorted(pool, key=lambda x: self._fitness(x, target))
            best_individual = pool[0]
            best_fitness = self._fitness(best_individual, target)
            if log:
                print(self._log_msg(gen_i, best_individual, best_fitness))
            if best_fitness <= 0:
                return pool
            pool = self._new_pool(pool)
        return pool
