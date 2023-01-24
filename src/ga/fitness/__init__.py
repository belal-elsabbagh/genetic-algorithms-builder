def match_target(individual, target):
    '''
    Calculate fitness score, it is the number of
    characters in string which differ from target
    string.
    '''
    fitness = 0
    for gs, gt in zip(individual.get_chromosome(), target):
        if gs != gt:
            fitness += 1
    return fitness
