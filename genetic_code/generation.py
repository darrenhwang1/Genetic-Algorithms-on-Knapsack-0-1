import random


def generate_first_random(k_problem):
    visited_indices, current_weight, str_rep = [], 0, ""
    current_solution = ["0" for i in range(len(k_problem[1]))]

    while True:

        if len(visited_indices) == len(k_problem[1]):
            break
        index = int(random.random() * len(k_problem[1]))
        if index in visited_indices:
            continue
        weight = k_problem[2][index]
        if current_weight + weight > k_problem[0]:
            break
        current_weight += weight
        visited_indices.append(index)
        current_solution[index] = "1"

    for i in range(len(current_solution)):
        str_rep += current_solution[i]

    return str_rep


def generate_n(k_problem, n):
    """
    Takes a example problem and returns n possible solutions
    :param k_problem: A knapsack problem returned by knapsack.generator()
    :param n: The number of solutions requested
    :return: A list of possible solutions in one-hot representation
    """
    return [generate_first_random(k_problem) for i in range(n)]




