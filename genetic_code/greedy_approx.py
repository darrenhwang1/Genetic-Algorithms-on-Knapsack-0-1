import sys


def sort_fuc(x):

    if x[1] == 0:
        return sys.maxint
    else:
        return float(x[0])/x[1]


def two_approx(k_problem):
    weights_value, capacity, curr_weight, counter, curr_value = zip(k_problem[1], k_problem[2]), k_problem[0], 0, 0, 0
    sorted_w_v = sorted(weights_value, key=sort_fuc, reverse=True)

    while True:
        if counter >= len(weights_value):
            return curr_value

        if curr_weight + sorted_w_v[counter][1] > capacity:
            if curr_value > sorted_w_v[counter][0]:
                return curr_value
            else:
                return sorted_w_v[counter][0]
        else:
            curr_weight += sorted_w_v[counter][1]
            curr_value += sorted_w_v[counter][0]
            counter += 1

