import time
import sys
import numpy as np
from simulation_client import body_request, set_configuration
from calculations import calculate_energy, collision, escape, runtime
from deap import base, creator, tools, algorithms
import grpc
from proto import simulation_pb2
from proto import simulation_pb2_grpc

sys.path.append("./proto")

def main():
    server_address = "0.0.0.0:50051"
    learning_rate = 0.1
    num_generations = 40
    population_size = 100
    crossover_prob = 0.5
    mutation_prob = 0.2
    individual_size = 4

    try:
        with grpc.insecure_channel(server_address) as channel:
            stub = simulation_pb2_grpc.SimStub(channel)

            def evaluate(individual):
                body_positions = np.array(individual)
                return (runtime(body_positions, stub),)

            creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
            creator.create("Individual", list, fitness=creator.FitnessMin)

            toolbox = base.Toolbox()
            toolbox.register("attr_float", np.random.uniform, -200, 200)
            toolbox.register("individual", tools.initRepeat, creator.Individual,
                             toolbox.attr_float, n=individual_size)
            toolbox.register("population", tools.initRepeat, list, toolbox.individual)

            toolbox.register("evaluate", evaluate)
            toolbox.register("mate", tools.cxBlend, alpha=0.5)
            toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=learning_rate, indpb=0.2)
            toolbox.register("select", tools.selTournament, tournsize=3)

            population = toolbox.population(n=population_size)

            fitnesses = list(map(toolbox.evaluate, population))
            for ind, fit in zip(population, fitnesses):
                ind.fitness.values = fit

            for gen in range(num_generations):
                offspring = toolbox.select(population, len(population))
                offspring = list(map(toolbox.clone, offspring))

                for child1, child2 in zip(offspring[::2], offspring[1::2]):
                    if np.random.rand() < crossover_prob:
                        toolbox.mate(child1, child2)
                        del child1.fitness.values
                        del child2.fitness.values

                for mutant in offspring:
                    if np.random.rand() < mutation_prob:
                        toolbox.mutate(mutant)
                        del mutant.fitness.values

                invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
                fitnesses = map(toolbox.evaluate, invalid_ind)
                for ind, fit in zip(invalid_ind, fitnesses):
                    ind.fitness.values = fit

                population[:] = offspring

            fits = [ind.fitness.values[0] for ind in population]

            print(f"Min runtime: {min(fits)}")
            print(f"Max runtime: {max(fits)}")
            print(f"Avg runtime: {sum(fits) / len(fits)}")

            best_ind = tools.selBest(population, 1)[0]
            print(f"Best individual: {best_ind}")
            print(f"Best fitness: {best_ind.fitness.values[0]}")

    except KeyboardInterrupt:
        print("[Agent] Stopping Agent")

if __name__ == "__main__":
    main()

