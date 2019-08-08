# initial file
import random
from ga import GA
print("Tangram Geenetic Algorithm Solver")

# TEST

# Valid genes
GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!\"#%&/()=?@${[]}"

TARGET = "Hello World"


def mutated_genes():
    gene = random.choice(GENES)
    return gene


def create_genome():
    gnome_len = len(TARGET)
    return [mutated_genes() for _ in range(gnome_len)]


def print_genome(genome):
    print("".join(genome))


def cal_fitness(genome):
    fitness = 0
    for gs, gt in zip(genome, TARGET):
        if gs != gt:
            fitness += 1
    return fitness


def crossover_operator(parent1, parent2, mutation_prob):
    child_chromosome = []
    for gp1, gp2 in zip(parent1, parent2):
        prob = random.random()

        # if prob is less than 0.45, insert gene
        # from parent 1
        if prob < (1-mutation_prob)/2:
            child_chromosome.append(gp1)

        # if prob is between 0.45 and 0.90, insert
        # gene from parent 2
        elif prob < 1-mutation_prob:
            child_chromosome.append(gp2)
        # Mutate with 0.1 probability
        else:
            child_chromosome.append(mutated_genes())
    return child_chromosome


print_genome(GA(create_genome, cal_fitness,
                crossover_operator, print_genome, 100, 1000))
