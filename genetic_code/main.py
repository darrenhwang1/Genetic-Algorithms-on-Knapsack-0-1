import matplotlib.pyplot as plt
import knapsack
import breeding
import fitness
import generation
import mutation
import greedy_approx
import processing

def generate_approx(num_gens, first_gen, problem, mutation_rate, percent_keep):
    """
    Takes number of generations to produce, the knapsack problem to solve, and the first generation
    :param num_gens: an integer representing how many generations there will be
    :param first_gen: list of one-hot solutions to the knapsack
    :param problem: 3-tuple of a knapsack problem
    :param mutation_rate: rate of mutation
    :param percent_keep: the top percentage of solutions to keep for the next generation
    :return: A one-hot representation of a solution to the problem
    """
    capacity, values, weights, size, curr_gen = problem[0], problem[1], problem[2], len(first_gen), first_gen

    for i in range(0, num_gens - 1):
        mutated_gen = mutation.mutate_gen(curr_gen, mutation_rate)
        chosen_children = fitness.random_children(mutated_gen, 2 * (size - int(percent_keep * size)), capacity, values, weights)
        curr_gen = processing.get_k_most_fit(curr_gen, capacity, values, weights, int(percent_keep * size))
        for j in range(0, len(chosen_children)/2, 2):
            curr_gen.append(breeding.breed(chosen_children[j], chosen_children[j + 1], 0, 1))

    return processing.get_most_fit(curr_gen, problem[0], problem[1], problem[2])



def main():
    approx_acc = 0
    for i in range(0, 50):
        problem = knapsack.generator_unsort(15, (10, 500), (10, 500), 700)
        first_gen = generation.generate_n(problem, 100)
        genetic_score = processing.get_score(generate_approx(400, first_gen, problem, 0.01, 0.10), problem[1])
        two_approx_score = greedy_approx.two_approx(problem)

        print("genetic score:" + str(genetic_score))
        print("approx score:" + str(two_approx_score))

        approx_acc += float(genetic_score)/two_approx_score

    print(approx_acc/50)


def my_plot(num_gens, num_examples):
    x_axis = range(num_gens)
    accuracy = [0 for _ in range(num_gens)]
    estimated = 0

    for _ in range(num_examples):
        problem = knapsack.generator_unsort(100, (10, 500), (10, 500), 700)
        first_gen = generation.generate_n(problem, 100)
        two_approx_score = greedy_approx.two_approx(problem)
        exact_score = knapsack.dp_solve(*problem)
        estimated += two_approx_score / float(exact_score)
        print("Estimate accuracy: " + str(two_approx_score / float(exact_score)))

        i = 0
        for gen in generate_epochs(num_gens, first_gen, problem, 0.01, 0.10):
            score = processing.get_score(gen, *problem)
            acc = score / float(exact_score)
            accuracy[i] += acc/float(num_examples)
            i += 1

    plt.plot(x_axis, accuracy)

    plt.xlabel('Generations')
    plt.ylabel('Accuracy')
    plt.show()

main()
