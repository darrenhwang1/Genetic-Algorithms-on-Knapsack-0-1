import knapsack
import breeding
import fitness
import generation
import mutation
import greedy_approx

##Gets the most fit solution out of a generation
def get_most_fit(gen, capacity, values, weights):
    max_val, best_gen, array_gen = 0, "", []

    for i in gen:
        if fitness.child_fitness(i, capacity, values, weights) >= max_val and get_weight(i, weights) <= capacity:
            max_val = fitness.child_fitness(i, capacity, values, weights)
            best_gen = i

    array_gen.append(best_gen)

    return best_gen

#Gets the score of a solution
def get_score(gen, values):
    score = 0
    for i, bit in enumerate(gen):
        if bit == "1":
            score += values[i]
    return score

#Grabs the k most fit solutions from a generation
def get_k_most_fit(gen, capacity, values, weights, k):
    sorted_gens = sorted(gen, key=lambda x: fitness_sort(x, capacity, values, weights), reverse=True)

    return sorted_gens[0:k]

#Computes weight of a solution
def get_weight(gen, weights):
    w = 0
    for i, bit in enumerate(gen):
        if bit == "1":
            w += weights[i]
    return w

#Sorts solutions of a generation by fitness
def fitness_sort(gen, capacity, values, weights):
    if get_weight(gen, weights) > capacity:
        return 0
    else:
        return fitness.child_fitness(gen, capacity, values, weights)