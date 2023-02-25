"""
Genetic Algorithm
"""
from .__base import GeneticAlgorithm
from .Individual import Individual, NumberIndividual


GeneticAlgorithm = GeneticAlgorithm


class NumberGeneticAlgorithm(GeneticAlgorithm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    @staticmethod
    def mutate(x):
        return NumberIndividual.fmt_mutation(x)
            


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
                print(self._log_msg(gen_i, best_individual,
                      best_fitness) + f'\tPool: {len(pool)}')
            if best_fitness <= 0:
                return pool
            pool = self._new_pool(pool)
        return pool
