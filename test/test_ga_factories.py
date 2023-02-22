from src.ga.Individual import Individual
from src.util import match_target
from src.ga.GeneticAlgorithmFactory import GeneticAlgorithmFactory
from src.ga.TargetMatchingGeneticAlgorithm import TargetMatchingGeneticAlgorithm

def test_generic_factory():
    ga = GeneticAlgorithmFactory().create(
        fitness=match_target,
        crossover=Individual.mate,
        mutate=lambda x: x.add_mutations([]),
        ga_type=TargetMatchingGeneticAlgorithm
    )
    assert ga is not None
    assert ga.get_crossover() is not None
    assert ga.get_fitness() is not None
    assert ga.get_mutate() is not None
    assert ga.get_select() is not None