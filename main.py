
# 

import random
import math

weight = 0.00
utility = 0.00
count = 0
one_gen = []
total_fitness = 0
#List to hold values of items.
utility_weight_list = []
while count < 1000:
    initial_pop = [0] * 400

    while sum(initial_pop) != 20:
        item = random.randint(0, 399)
        if initial_pop[item] == 0:
            initial_pop[item] = 1

    one_gen.append(initial_pop)
    count += 1

with open("Program2Input.txt") as file:

    for data in file:
        utility_weight_list.append(data.split())

for i in range(0, 999): #one_gen indexing
    fitness_score = 0
    total_weight = 0
    sum_utilities = 0
    for j in range(0, len(one_gen[i]) - 1): #initial_pop indexing
        if one_gen[i][j] == 1:
            total_weight += float(utility_weight_list[j][1])
            sum_utilities += float(utility_weight_list[j][0])

        else:
            continue
    if total_weight > 500:
        fitness_score = 1
        total_fitness += fitness_score
    else:
        fitness_score = sum_utilities
        total_fitness += fitness_score

#L2 Distribution
for i in range(0, 999):
    L2_fitness = 0
    for j in range(0, len(one_gen[i]) - 1): #initial_pop indexing
        if one_gen[i][j] == 1:
            total_weight += float(utility_weight_list[j][1])
            sum_utilities += float(utility_weight_list[j][0])
            if total_weight > 500:
                fitness_score = 1

            else:
                fitness_score = sum_utilities









