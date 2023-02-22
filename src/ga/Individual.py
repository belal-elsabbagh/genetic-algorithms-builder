"""
This module contains the Individual class.
"""


import random


class Individual(object):
    """Individual class."""

    def __init__(self, chromosome: list = None):
        if chromosome is None:
            chromosome = []
        self._chromosome = chromosome
        """Initialize the Individual class."""

    def get_chromosome(self):
        """Return the chromosome of the individual."""
        return self._chromosome

    @classmethod
    def random_population(cls, size: int, target_size, genes):
        """Create a random population of individuals."""
        return [cls([random.choice(genes) for _ in range(target_size)]) for _ in range(size)]
    
    @classmethod
    def mate(cls, par1, par2):
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
                child_chromosome.append(None)
        return cls(child_chromosome)

    def __add__(self, other):
        return self.__class__.mate(self, other)

    def add_mutations(self, genes):
        """Add mutations to the individual."""
        self._chromosome = [random.choice(
            genes) if v is None else v for v in self._chromosome]
        return self


class NumberIndividual(Individual):
    def __init__(self, chromosome: float | int | list = None):
        chromosome = self.__bin_str(chromosome) if self.__is_number(chromosome) else chromosome 
        super().__init__(chromosome)

    @classmethod
    def __bin_str(cls, n: float | int) -> str:
        return f"{int(str(round(n, 2)).replace('.', '')):b}"
    
    @staticmethod
    def __is_number(n) -> bool:
        return type(n) is int or type(n) is float
    
    @classmethod
    def random_population(cls, size: int, genes):
        """Create a random population of individuals."""
        return [cls(random.choice(genes)) for _ in range(size)]

    def __str__(self) -> str:
        return f"{self.__float__()}"

    def __repr__(self) -> str:
        return str(self)

    def __float__(self) -> float:
        return float(int("".join([str(i) for i in self._chromosome]), 2))

    def __int__(self) -> int:
        return int("".join([str(i) for i in self._chromosome]), 2)
