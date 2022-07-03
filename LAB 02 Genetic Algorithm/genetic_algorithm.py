import random
import math


class GeneticAlgorithm:
    def __init__(self, problem, goal):
        self.problem = problem
        self.goal = goal
        self.population = None
        self.max_fitness = -math.inf
        self.score = 0
        self.generation = 1
        self.iteration_threshold = 200
        self.population_size = 16
        self.fittest_individual = False

    def run(self):
        self.population = [[random.randint(0, 1) for j in range(
            len(self.problem))] for i in range(self.population_size)]
        # print(f"{self.population}")
        while self.generation < self.iteration_threshold:
            print(f"GENERATIONS: {self.generation}")
            self.__select()
            if self.fittest_individual:
                print([self.problem[i][0] for i in range(len(self.problem))])
                print(f"FITTEST COMBINATION: {self.fittest_individual}")
                return
            # perform crossover among the parents from the first half of the population
            l, r = 0, len(self.population) // 2 - 1
            while l < r:
                offsprings = self.__crossover(
                    self.population[l], self.population[r])
                self.population[l], self.population[r] = offsprings[0], offsprings[1]
                l += 1
                r -= 1
            # randomly generate new population for second half of the array
            start_second_half = len(self.population) // 2
            for i in range(start_second_half, len(self.population)):
                self.population[i] = [random.randint(
                    0, 1) for j in range(len(self.problem))]
            # Perform mutation
            self.__mutate()
            self.generation += 1
        print([self.problem[i][0] for i in range(len(self.problem))])
        print(f"FAILURE: {-1}")

    def __select(self):
        fitness_list = self.__fitness()
        population_based_on_fitness = [i for _, i in sorted(
            zip(fitness_list, self.population))]
        population_based_on_fitness.reverse()
        self.population = population_based_on_fitness

    def __crossover(self, p1, p2):
        new_chromosome_set = [[], []]
        start = random.randint(0, len(p1)//2)
        end = start + len(p1) // 2
        for i in range(len(p1)):
            if start <= i < end:
                new_chromosome_set[0].append(p1[i])
                new_chromosome_set[1].append(p2[i])
            else:
                new_chromosome_set[0].append(p2[i])
                new_chromosome_set[1].append(p1[i])
        return new_chromosome_set

    def __mutate(self):
        # Perform mutation with very low probability to avoid premature convergence
        mutation_indices = [random.randint(
            0, len(self.population) - 1) for _ in range(5)]
        for index in mutation_indices:
            mutation_spot = random.randint(0, len(self.problem) - 1)
            self.population[index][mutation_spot] = 1 if self.population[index][mutation_spot] == 0 else 0

    def __fitness(self):
        fitness_list = []
        for chromosome in self.population:
            total_run = 0
            for i in range(len(chromosome)):
                total_run += chromosome[i] * self.problem[i][1]
            difference = abs(self.goal - total_run)
            if difference == 0:
                self.max_fitness = math.inf
                self.fittest_individual = chromosome
                fitness_list.append(math.inf)
            else:
                fitness_list.append(1/difference)
        return fitness_list


def read_from_console():
    n, target_run = input().split()
    n, target_run = int(n), int(target_run)
    batsmen = []
    for _ in range(n):
        batsman, average_run = input().split()
        batsmen.append((batsman, int(average_run)))
    return batsmen, target_run


""" Driver Code """

if __name__ == '__main__':
    problem, target_run = read_from_console()
    genetic_algorithm = GeneticAlgorithm(problem, target_run)
    genetic_algorithm.run()
