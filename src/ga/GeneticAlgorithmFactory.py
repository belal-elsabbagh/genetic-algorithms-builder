from src.ga.GeneticAlgorithm import GeneticAlgorithm


class GeneticAlgorithmFactory(object):
    """Factory class for Genetic Algorithm objects."""

    def __init__(self):
        """Initialize the factory class."""
        pass

    def create(
        self,
        encode: callable,
        decode: callable,
        validate: callable,
        fitness,
        crossover,
        mutate,
        select
    ) -> GeneticAlgorithm:
        """Create a Genetic Algorithm object."""
        return GeneticAlgorithm(
            encode=encode,
            decode=decode,
            validate=validate,
            fitness=fitness,
            crossover=crossover,
            mutate=mutate,
            select=select
        )
