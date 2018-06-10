### Project Members
[Aditi Agarwal](aditiagarwal2020@u.northwestern.edu), Ronit Basu, Lukas Gross, Darren Hwang

EECS 349 Northwestern University
### Abstract
Our task is to generate approximation solutions to instances of the 0-1 knapsack problem based on improving generations in a genetic algorithm. The task is important because the 0-1 knapsack problem lies in the set of problems with no known polynomial time solution. If a genetic algorithm solution can match or exceed current approximation algorithms, current applications of the knapsack problem (efficient resource allocation) could be better solved using our algorithm. 

Genetic algorithms are an obvious fit for such a problem due to the 0-1 knapsack problem being a paradigm of combinatorial optimization problem. To achieve the best results we tailored each part of the algorithm to meet our specific needs after iteratively testing each alternative (Elaborated on in the pdf). We use the 2-Approximation Algorithm as the approximation algorithm to compare.

To extract relevant insights from our results we narrowed down the domain of our problem. We begin by defining a scope for the problem we are solving by diving knapsack problems into 3 categories: small items relative to weight (Small), large items relative to weight (Large), small and large items relative to weight (Mixed Bag). 

### Results
![Results](./images/Results_Table.png)

In all three cases our algorithm beat popular greedy approximation algorithms as long as the number of generations was in the vicinity of ![n^2](./images/n2.png) where n is the number of items in the knapsack. In the interest of time we used ![n^2/2](./images/n2.png)/2 generations to approximate the results of the algorithm. The best result was achieved for Large problems where our genetic algorithm achieved a score 4.4% higher on average than the approximation algorithm.



## Detailed Report

### Introduction
We seek to use genetic algorithms to generate approximate solutions to knapsack 0-1 which can beat current approximation algorithms. Today, genetic algorithms are used to generate optimal solutions. The genetic algorithm first chooses parents at random. The parents are then used to produce children for successive generations. At each generation, an optimized solution is created from the given population.

### Definition of the problem
![knapsack def](./images/knapsack_def.png)


### Knapsack Representation
We represent a solution to a knapsack problem using weight arrays, value arrays, and a corresponding bit array.

Suppose we have a knapsack with capacity 15, and 4 items: (15, 4), (2, 10), (8, 7), (9, 2) where the first number of any pair is the value of the item and the second number is the weight. 

#### Value Array
![weight_array](./images/weight_vector.png)

#### Weight Array
![value_array](./images/value_vector.png)

#### Bit Array
![bit_array](./images/bit_vector.png)

This Bit array represents a knapsack solution that takes two items - the first item with value of 10 and weight of 2, and the second item with value of 7 and weight of 8.

### Dataset Generation

### First Generation

## Tuning Parameters

### Fitness Functions

### Selection

### Crossover

### Mutation

### Final Results

### Complexity Analysis

