import random
import math


# Takes in capacity, array of values and wights for a child and returns a fitness
def fitness_function_log(capacity, child_values, child_weights):
    result = math.log(sum(child_values), 2)
    weight_sum = sum(child_weights)
    if weight_sum > capacity:
        return 0

    return result


def fitness_function_linear(capacity, child_values, child_weights):
    result = sum(child_values)
    weight_sum = sum(child_weights)
    if weight_sum > capacity:
        return 0

    return result


def fitness_function_exponential(capacity, child_values, child_weights):
    result = sum(child_values)
    weight_sum = sum(child_weights)
    if weight_sum > capacity:
        if weight_sum >= (2 * capacity):
            return 0
        else:
            percent = 2 - float(weight_sum)/capacity
            percent = math.pow(percent, 2)
            return percent * result

    return result


def child_fitness(child, capacity, values, weights):
    child_values, child_weights = [], []
    for i, bit in enumerate(child):
        if bit == "1":
            child_values.append(values[i])
            child_weights.append(weights[i])

    return fitness_function_exponential(capacity, child_values, child_weights)


def get_fitness_values(children, capacity, values, weights):
    fitness_values = [child_fitness(child, capacity, values, weights) for child in children]
    for i in range(1, len(fitness_values)):
        fitness_values[i] += fitness_values[i - 1]

    return fitness_values


def random_child(children, fitness_values):
    index = random.uniform(fitness_values[0], fitness_values[-1])
    for i, fitness_value in enumerate(fitness_values):
        if fitness_value > index:
            return children[i - 1]

    return children[-1]


def random_children(children, num_random_children, capacity, values, weights):
    """
    Returns a list of random children with each child having a wighted chance of being picked. Can return duplicates.
    :param children: A list of children represented by a one-hot bit string
    :param num_random_children: The number of random children to return
    :param capacity: Capacity of this example
    :param values: The values list of this example
    :param weights: The weights list of this example
    :return: A list of num_random_children random children, each represented by a one-hot bit string
    """
    fitness_values = get_fitness_values(children, capacity, values, weights)

    return [random_child(children, fitness_values) for i in range(num_random_children)]