
# Timothy Hoang CS 461- Program 2

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

def New_Parent(lst, old_parent):
    new_parent = []
    random_float = random.random()
    for i, value in enumerate(lst):

        if value > random_float:
            new_parent.extend(old_parent)
            return new_parent

def Mutate_Gene(child):
    for i in range(0, len(child)):
        mutation = random.randint(1, 10000)
        if mutation == 1:
            if child[i] == 1:
                child[i] = 0
            else:
                child[i] = 1
    return child

## Read Data from file.
utility_weight_list = []
gen_size = 1000
pop_size = 400
start_pop = 500
generations = 5000
max_fitness_list = []
average_fitness_list = []
count = 0
with open("Program2Input.txt") as file:

    for data in file:
        utility_weight_list.append(data.split()) #list holding all data

one_gen = Generate_Pop(gen_size, pop_size)  ##first generation

## Iterate on generations count
while count < generations:
    average_fitness = 0
    max_fitness = 0
    child_list = []
    count_1 = 0
    new_parents = []

    fitness_list = Fitness_Func(one_gen, utility_weight_list)  # list of all fitness score


    squared_fitness = [pow(fitness, 2) for fitness in fitness_list]


    L2_list = L2_Func(squared_fitness) ## lsit of all L2 probabilities

    CDF_values = CDF_Func(L2_list)
    new_parents = New_Parent(CDF_values, one_gen)

    while count_1 < start_pop:

        ## trying to splice up DNA and make children
        random_gen_index = random.randint(0, len(new_parents) - 1)
        random_child_value = random.randint(0, pop_size - 1)

        new_child_1 = (one_gen[random_gen_index][random_child_value:] + new_parents[random_gen_index][:random_child_value])


        new_child_2 = (one_gen[random_gen_index][:random_child_value] + new_parents[random_gen_index][random_child_value:])

        ## mutate 1/10000.
        new_child_1 = Mutate_Gene(new_child_1)
        new_child_2 = Mutate_Gene(new_child_2)

        child_list.append(new_child_1)
        child_list.append(new_child_2)
        count_1 += 1


    one_gen = child_list #set new children list as the generation

    ## try to keep trach of max and average fitness
    average_fitness = sum(fitness_list) / len(fitness_list)
    average_fitness_list.append(average_fitness)
    max_fitness = max(fitness_list)
    max_fitness_list.append(max_fitness)

    #test each iteration
    print("Max fitness gen ", count, " : ", max_fitness)
    print("Average fitness gen ", count, " :", average_fitness)

    f = open("outputfile.txt", "w")
    L = ["Generation ", str(generations), "\nMax per generation: ", str(max_fitness), "\nAverage per generation: ", str(average_fitness)]
    f.writelines(L)
    f.close()
    count += 1

print("Starting population: ", start_pop)
print("Max fitness after ", generations, " generations: ", max_fitness_list[len(max_fitness_list) - 1])
print("Average fitness: ", average_fitness_list[len(average_fitness_list) - 1])



## Roll for Mutation 1/10000(0.00001) Success roll = flip random -> repeat one generation -> repeat program.

## record average fitness and max fitness





