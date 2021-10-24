
# 

import random
import math

def Generate_Pop(gen_size, pop_size):
    one_gen = []
    count = 0
    while count < gen_size:
        initial_pop = [0] * pop_size

        while sum(initial_pop) < (pop_size / 20):
            item = random.randint(0, pop_size - 1)
            if initial_pop[item] == 0:
                initial_pop[item] = 1

        one_gen.append(initial_pop)
        count += 1
    return one_gen

## Calculate fitness for L2 and also sum of fitness
def Fitness_Func(gen_list, data_list):

    list_of_fitness = []
    for i in range(0, len(gen_list)): #one_gen indexing
        fitness_score = 0
        total_weight = 0
        for j in range(0, len(one_gen[i])): #initial_pop indexing
            if one_gen[i][j] == 1:
                total_weight += float(data_list[j][1])
                fitness_score += float(data_list[j][0])
            if total_weight > 500:
                fitness_score = 1
        list_of_fitness.append(fitness_score)
    return list_of_fitness

def L2_Func(list):
    L2 = []
    L2_dis = 0
    for fit in list:
        L2_dis = fit / sum(list)
        L2.append(L2_dis)
    return L2

def CDF_Func(lst):

    for i in range(1, len(lst)):
        lst[i] += lst[i - 1]
    return lst

def New_Parent(lst):
    new_parent = []
    random_float = random.random()
    for i, value in enumerate(lst):

        if value > random_float:
            new_parent.extend(one_gen[i:])
    return new_parent

## Read Data from file.
utility_weight_list = []

with open("Program2Input.txt") as file:

    for data in file:
        utility_weight_list.append(data.split()) #list holding all data

## generate generation and population using sizes.
one_gen = Generate_Pop(1000, 400)  ##first generation

# total_fitness, sum_of_fitness = Fitness_Func(one_gen, utility_weight_list) #total_fitness ** 2

fitness_list = Fitness_Func(one_gen, utility_weight_list)  # list of all fitness score

squared_fitness = [pow(fitness, 2) for fitness in fitness_list]

L2_total_fitness = 0

L2_list = L2_Func(squared_fitness) ## lsit of all L2 probabilities

CDF_values = CDF_Func(L2_list)
new_p = New_Parent(CDF_values)

random_child_value = random.randint(0, 400)

new_child_1 = (one_gen[random_child_value:] + new_p[:random_child_value])

new_child_2 = (one_gen[:random_child_value] + new_p[random_child_value:])

### Splice DNA and create 2 children (crossover)

## Roll for Mutation 1/10000(0.00001) Success roll = flip random -> repeat one generation -> repeat program.





