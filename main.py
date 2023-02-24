"""Main module for the genetic algorithm project."""

import string
from src.ga import GeneticAlgorithmFactory
from src.ga.TargetMatchingGeneticAlgorithm import TargetMatchingGeneticAlgorithm
from src.ga.GeneticAlgorithm import NumberGeneticAlgorithm
from src.ga.Individual import Individual, NumberIndividual
from src.util import match_target


CHARACTERS = string.ascii_lowercase + ' '


if __name__ == '__main__':
    target = "covenant of the deep"
    ga = GeneticAlgorithmFactory().create(
        fitness=match_target,
        crossover=Individual.mate,
        mutate=lambda x: x.add_mutations(CHARACTERS),
        ga_type=TargetMatchingGeneticAlgorithm,
        select=lambda x: x[:int(len(x)*0.05)]
    )
    population = Individual.random_population(20, len(target), CHARACTERS)
    res = ga.run(population, 1000, target, log=True)
    print(f"Answer: {res[0].get_chromosome()}")
    
    ga = NumberGeneticAlgorithm(
        fitness=lambda x: abs(25 - float(x)*float(x)),
        crossover=lambda x, y: x + y,
        mutate=lambda x: NumberIndividual(str("".join([str(i) for i in x.get_chromosome()])).replace('None', '0')),
        select=lambda x: x[:int(len(x)*0.05)],
    )
    population = NumberIndividual.random_population(50, list(range(200)))
    res = ga.run(population, 200, True)
    print(f"Answer: {float(res[0])}")
    
    
