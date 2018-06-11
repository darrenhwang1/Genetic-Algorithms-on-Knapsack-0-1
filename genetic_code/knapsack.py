import random


def generator_unsort(size, value_range, weight_range, capacity=None):
    """
    Returns a randomized example problem
    :param size: Number of items e.g. 100
    :param value_range: Range of values e.g. (0, 1000)
    :param weight_range: Range of weights e.g. (100, 1000)
    :param capacity: (Optional) Total knapsack capacity e.g. 100
    :return: (capacity, list of values, list of weights)
    """
    lower_capacity_bound = (weight_range[1] - weight_range[0]) / 2
    if capacity is None:
        capacity = random.randrange(lower_capacity_bound, weight_range[1] * 10)
    values = [random.randrange(value_range[0], value_range[1]) for i in xrange(size)]
    weights = [random.randrange(weight_range[0], weight_range[1]) for i in xrange(size)]

    return capacity, values, weights


def sort_knapsack_problem(knapsack):
    value_weights = zip(*sorted(zip(knapsack[1], knapsack[2]), key=lambda x: x[1]))

    return knapsack[0], value_weights[0], value_weights[1]


def generator_sort(size, value_range, weight_range, capacity=None):

    return sort_knapsack_problem(generator_unsort(size, value_range, weight_range, capacity))


def dp_solve(capacity, values, weights):
    length, result, w = len(values), 0, capacity
    table = [[0 for i in xrange(capacity + 1)] for j in range(0, len(capacity) + 1)]

    for i in range(1, length + 1):
        weight, value = weights[i - 1], values[i - 1]
        for w in range(1, capacity + 1):
            if weight > w:
                table[i][w] = table[i - 1][w]
            else:
                table[i][w] = max(table[i - 1][w],
                                  table[i - 1][w - weight] + value)

    for i in range(length, 0, -1):
        if table[i][w] != table[i - 1][w]:
            weight = weights[i - 1]
            value = values[i - 1]
            result += value
            w -= weight

    return result


def dp_solve_recursive(capacity, values, weights, n=None):
    if n is None:
        n = len(values)
    if n == 0 or capacity == 0:
        return 0

    without_nth = dp_solve_recursive(capacity, values, weights, n-1)

    if weights[n-1] > capacity:
        return without_nth

    with_nth = values[n-1] + dp_solve_recursive(capacity - weights[n-1], values, weights, n-1)

    return max(with_nth, without_nth)
