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

    @staticmethod
    def _create_child_chromosome(c1, c2):
        child1, child2 = [], []
        for gp1, gp2 in zip(c1, c2):
            prob = random.random()
            if prob < 0.5:
                child1.append(gp1)
                child2.append(gp2)
            else:
                child1.append(gp2)
                child2.append(gp1)
        return child1, child2

    @classmethod
    def mate(cls, par1, par2):
        '''
        Perform mating and produce new offspring
        '''
        c1, c2 = cls._create_child_chromosome(par1.get_chromosome(), par2.get_chromosome())
        return cls(c1), cls(c2)

    def __add__(self, other):
        return self.__class__.mate(self, other)

    def add_mutations(self, genes):
        """Add mutations to the individual."""
        self._chromosome[random.randint(0, len(self._chromosome) - 1)] = random.choice(genes)
        return self
    
    @staticmethod
    def mutate(x):
        index = random.randint(0, len(x.get_chromosome()) - 1)
        x.get_chromosome()[index] = 1 - x.get_chromosome()[index]
        return x


def bin_str(n: float | int) -> str:
    return f"{int(str(round(n, 2)).replace('.', '')):b}"


class NumberIndividual(Individual):
    def __init__(self, chromosome: float | int | list = None):
        chromosome = [int(i) for i in bin_str(chromosome)] if self._is_number(
            chromosome) else chromosome
        super().__init__(chromosome)

    @staticmethod
    def _is_number(n) -> bool:
        return type(n) is int or type(n) is float

    @staticmethod
    def fmt_bin_str(s):
        return "".join([str(i) for i in s])

    @classmethod
    def random_population(cls, size: int, genes):
        """Create a random population of individuals."""
        return [cls(random.choice(genes)) for _ in range(size)]

    def __str__(self) -> str:
        return f"{self.__float__()}"

    def __repr__(self) -> str:
        return str(self)

    def __float__(self) -> float:
        return float(int(self.fmt_bin_str(self._chromosome), 2))

    def __int__(self) -> int:
        return int(self.fmt_bin_str(self._chromosome), 2)


class NSpacePointIndividual(Individual):
    __n: int = 0

    def __init__(self, chromosome: list = None):
        self.__n: int = len(chromosome)
        c = [bin_str(i) for i in chromosome] if all(
            [isinstance(item, int) for item in chromosome])else chromosome
        super().__init__(c)

    def n(self) -> int:
        return self.__n

    def __add__(self, other):
        if self.n() != other.n():
            raise ValueError("Both individuals must have the same dimensions")
        return self.__class__([
            self._create_child_chromosome(dim1, dim2)
            for dim1, dim2 in zip(self.get_chromosome(), other.get_chromosome())
        ])

    @classmethod
    def random_population(cls, size: int, genes, n_dim):
        """Create a random population of individuals."""
        return [cls([random.choice(genes) for _ in range(n_dim)]) for _ in range(size)]

    def dim(self, ind):
        c = NumberIndividual.fmt_bin_str(self._chromosome[ind])
        if '-' in c:
            return - int(c[1:],2)
        return int(NumberIndividual.fmt_bin_str(self._chromosome[ind]), 2)

    @classmethod
    def mutate(cls, x):
        return cls([NumberIndividual.fmt_mutation(i) for i in x.get_chromosome()])

    def point(self):
        return [int(NumberIndividual.fmt_bin_str(i), 2) for i in self._chromosome]


class KnapsackIndividual(Individual):
        def __init__(self, chromosome: list = None):
            super().__init__(chromosome)
            
        @classmethod
        def random_population(cls, size: int, genes):
            """Create a random population of individuals."""
            return [cls([random.choice([0, 1]) for _ in range(len(genes))]) for _ in range(size)]
        
        def __add__(self, other):
            return self.__class__.mate(self, other)
        
        def render_items(self, items):
            return [items[i] for i, x in enumerate(self.get_chromosome()) if x == 1]
        
        def fitness(self, items):
            return sum([x[1] for x in self.render_items(items)])
        
        def weight(self, items):
            return sum([x[0] for x in self.render_items(items)])
        
        def render(self, items) -> str:
            d = {'Weight': self.weight(items), 'Value': self.fitness(items)}
            return f"{d}"
        
        
        
        
           
        
        