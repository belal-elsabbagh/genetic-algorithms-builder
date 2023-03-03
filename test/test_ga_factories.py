from src.ga.individual import Individual
from src.ga import GeneticAlgorithm
from src.ga import TargetMatchingGeneticAlgorithm

def test_generic_factory():
    ga = GeneticAlgorithm.create(
        fitness=TargetMatchingGeneticAlgorithm.match_target,
        crossover=Individual.mate,
        mutate=lambda x: x.add_mutations([]),
    )
    assert ga is not None
    assert ga.get_crossover() is not None
    assert ga.get_fitness() is not None
    assert ga.get_mutate() is not None
    assert ga.get_select() is not None
