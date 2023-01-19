"""Main module for the genetic algorithm project."""

from src.ga import GeneticAlgorithmFactory


if __name__ == '__main__':
    factory = GeneticAlgorithmFactory()
    ga = factory.create(
        encode=lambda x: "{0:b}".format(x),
        decode=lambda x: int(x, 2),
        validate=lambda x: x,
        fitness=lambda x: x,
        crossover=lambda x: x,
        mutate=lambda x: x,
        select=lambda x: x
    )
    print(ga.run([1, 2, 3, 4, 5], 10))
