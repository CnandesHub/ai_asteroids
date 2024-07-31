import numpy as np
from utils import lerp
from copy import copy


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
            self.genes[i] = lerp(self.genes[i], np.random.uniform(-1, 1), mutation_rate)
            # if np.random.rand() < mutation_rate:
            #     self.genes[i] = np.random.uniform(-1, 1)

    def get_genes(self):
        return self.genes


class Population:
    def __init__(self, mutation_rate, population, scores):
        self.population = population
        self.scores = scores
        self.mutation_rate = mutation_rate
        self.best_individual = None
        self.best_score = float("-inf")

    def evolve(self):
        new_generation = []

        # Calculate fitness
        fitness_scores = self.scores
        sum_fitness = sum(fitness_scores)
        if sum_fitness == 0:
            return

        # Normalize fitness scores
        normalized_fitness = [score / sum_fitness for score in fitness_scores]

        # Find the best individual in the population
        best_index = np.argmax(self.scores)
        best_individual = self.population[best_index]
        best_score = self.scores[best_index]

        # Keep the best individuals in the population
        # new_generation.append(best_individual)
        num_best_individuals = int(len(self.population) * 0.3)
        sorted_indices = np.argsort(self.scores)[::-1][:num_best_individuals]
        for index in sorted_indices:
            new_generation.append(self.population[index])

        # Create new generation using roulette wheel selection
        for _ in range(len(self.population) - num_best_individuals):
            individual = self.roulette_wheel_selection(normalized_fitness)
            individual.mutate(self.mutation_rate)
            new_generation.append(individual)

        self.population = new_generation
        self.best_individual = best_individual
        self.best_score = best_score

    def roulette_wheel_selection(self, normalized_fitness):
        index = 0
        r = np.random.rand()
        while r > 0:
            r -= normalized_fitness[index]
            index += 1
        index -= 1
        return copy(self.population[index])
