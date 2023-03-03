"""Main module for the genetic algorithm project."""

import math
import string
from src.ga import NumberGeneticAlgorithm, KnapsackGeneticAlgorithm
from src.ga.individual import NSpacePointIndividual, NumberIndividual, KnapsackIndividual


CHARACTERS = string.ascii_lowercase + ' '


if __name__ == '__main__':
    ga = KnapsackGeneticAlgorithm(
        items=[
            [1, 2],
            [2, 4],
            [3, 4],
            [4, 5],
            [5, 7],
            [6, 9]
        ],
        max_weight=10,
        crossover=lambda x, y: x + y,
        mutate=lambda x: x,
        select=lambda x: x[:int(len(x)*0.05)]
    )
    population = KnapsackIndividual.random_population(10, ga.items)
    res = ga.run(population, 200, debug=True)
    print(f"Answer: {res[0].render(ga.items)}")

    # ga = NumberGeneticAlgorithm(
    #     fitness=lambda x: abs(25 - float(x)*float(x)),
    #     crossover=lambda x, y: x + y,
    #     mutate=lambda x: NumberIndividual(str("".join([str(i) for i in x.get_chromosome()])).replace('None', '0')),
    #     select=lambda x: x[:int(len(x)*0.05)],
    # )
    # population = NumberIndividual.random_population(50, list(range(30)))
    # res = ga.run(population, 200, debug=True)
    # print(f"Answer: {float(res[0])}")

    # ga = NumberGeneticAlgorithm(
    #     fitness=lambda x: math.sin(math.sqrt(x.dim(0) ** 2 + x.dim(1) ** 2)),
    #     crossover=lambda x, y: x + y,
    #     mutate=NSpacePointIndividual.mutate,
    #     select=lambda x: x[:int(len(x)*0.05)],
    # )
    # population = NSpacePointIndividual.random_population(50, list(range(-4, 5)), 2)
    # res = ga.run(population, 200, debug=True, zero_best=False, max_fitness=True)
    # print(f"Answer: {res[0].point()}")
