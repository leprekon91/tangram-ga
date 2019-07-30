# General GA Implementation
import random
import numpy as np

ELITISM = .1
MUTATION_PROB = .1

def init_population(gene_creator, size):
    populous = []
    for _ in range(size):
        genome = gene_creator()
        populous.append(genome)
    return populous


def GA(gene_creator, fitness, crossover, print_genome, size,max_generations):
    # current generation
    generation = 1

    # found the best genome
    found = False

    # initialize population
    population = []
    population = init_population(gene_creator, size)
    x=np.array([])
    y= np.array([])

    # GA LOOP:
    while not found and generation < max_generations:
        # sort the genomes by their fitness
        population = sorted(population, key=lambda X: fitness(X))
        if fitness(population[0]) <= 0:
            found = True
            break

        new_generation = []

        # Perform Elitism, that mean 20% of fittest population
        # goes to the next generation
        s = int(ELITISM*size)
        new_generation.extend(population[:s])

        # Recreate the population size in new generation,
        # by mating parents from the fittest 50% of the population
        s = int((1-ELITISM)*size)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = crossover(parent1, parent2,MUTATION_PROB)
            new_generation.append(child)

        population = new_generation

        print("Generation #{}\tFitness: {}\n".format(
            generation, str(fitness(population[0]))))
        
        #print_genome(population[0])

        generation += 1

    return population[0]
