import random


def mutate(child, p):
    """
    Takes a a child and a threashold probability and returns a mutated child
    :param child: The input child
    :param p: Threshold probability (0, 1) that any given bit is mutated
    :return: Mutated child (one-hot representation)
    """

    child_arr, mutant = [], []

    for bit in child:
        if bit == "1":
            child_arr.append(1)
        else:
            child_arr.append(0)

    for bit in child_arr:
        if random.random() <= p:
            if bit == 1:
                mutant.append(0)
            if bit == 0:
                mutant.append(1)
        else:
            mutant.append(bit)

    mutant = "".join(map(str, mutant))

    return mutant


def mutate_gen(gen, p):
    mutated_gen = []
    for i in gen:
        mutated_gen.append(mutate(i, p))

    return mutated_gen
