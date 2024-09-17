import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
target_word = "METHINKS IT IS LIKE A WEASEL"
population_size = 100
mutation_rate = 0.01

def generate_random_string(length):
    return ''.join(random.choice(characters) for _ in range(length))

def calculate_fitness(word):
    return sum(1 for expected, actual in zip(target_word, word) if expected == actual)

def mutate(word):
    return ''.join(random.choice(characters) if random.random() < mutation_rate else char for char in word)

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(target_word) - 1)
    return parent1[:crossover_point] + parent2[crossover_point:]

# Initialize population
population = [generate_random_string(len(target_word)) for _ in range(population_size)]

while True:
    # Calculate fitness for each individual
    population = sorted(population, key=lambda word: calculate_fitness(word), reverse=True)
    best_individual = population[0]
    print("Best individual:", best_individual, "Fitness:", calculate_fitness(best_individual))

    # Check if we have found the solution
    if best_individual == target_word:
        break

    # Create new population
    new_population = []
    for _ in range(population_size // 2):
        parent1 = random.choice(population[:50])
        parent2 = random.choice(population[:50])
        child1 = mutate(crossover(parent1, parent2))
        child2 = mutate(crossover(parent2, parent1))
        new_population.extend([child1, child2])

    population = new_population
