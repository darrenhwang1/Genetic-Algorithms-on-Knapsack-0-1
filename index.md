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

