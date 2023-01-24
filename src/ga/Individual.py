"""
This module contains the Individual class.
"""


import random


class Individual(object):
    """Individual class."""

    def __init__(self, chromosome: list = None):
        if chromosome is None:
            chromosome = []
        self.__chromosome = chromosome
        """Initialize the Individual class."""

    def get_chromosome(self):
        """Return the chromosome of the individual."""
        return self.__chromosome

    @staticmethod
    def random_population(size: int, target_size, genes):
        """Create a random population of individuals."""
        return [Individual([random.choice(genes) for _ in range(target_size)]) for _ in range(size)]

    def add_mutations(self, genes):
        """Add mutations to the individual."""
        self.__chromosome = [random.choice(
            genes) if v is None else v for v in self.__chromosome]
        return self
