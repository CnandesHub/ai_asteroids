import numpy as np


class DNA:
    def __init__(self, length):
        self.genes = np.random.uniform(-1, 1, length)

    def crossover(self, partner):
        child = DNA(len(self.genes))
        midpoint = np.random.randint(0, len(self.genes))

        # Crossover
        child.genes[:midpoint] = self.genes[:midpoint]
        child.genes[midpoint:] = partner.genes[midpoint:]
        return child

    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            if np.random.rand() < mutation_rate:
                self.genes[i] = np.random.uniform(-1, 1)

    def get_genes(self):
        return self.genes


class Population:
    def __init__(self, pop_size, mutation_rate):
        self.population = [DNA(length=10) for _ in range(pop_size)]
        self.mutation_rate = mutation_rate

    def evolve(self):
        new_generation = []

        # Calculate fitness
        fitness_scores = [
            self.calculate_fitness(individual) for individual in self.population
        ]
        max_fitness = max(fitness_scores)
        print("Max Fitness:", max_fitness)

        # Normalize fitness scores
        normalized_fitness = [score / max_fitness for score in fitness_scores]

        # Create new generation using roulette wheel selection
        for _ in range(len(self.population)):
            # Select two parents based on their fitness
            parent1 = self.roulette_wheel_selection(normalized_fitness)
            parent2 = self.roulette_wheel_selection(normalized_fitness)

            # Crossover and mutate to create child
            child = parent1.crossover(parent2)
            child.mutate(self.mutation_rate)
            new_generation.append(child)

        self.population = new_generation

    def roulette_wheel_selection(self, normalized_fitness):
        index = 0
        r = np.random.rand()
        while r > 0:
            r -= normalized_fitness[index]
            index += 1
        index -= 1
        return self.population[index]

    def calculate_fitness(self, individual):
        pass
