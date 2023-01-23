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
    def create_random_population(size: int, create_random_individual):
        """Create a random population of individuals."""
        return [create_random_individual() for _ in range(size)]
