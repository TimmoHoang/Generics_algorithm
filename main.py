
# 

import random

weight = 0.00
utility = 0.00
count = 0
one_gen = []


while count < 1000:
    initial_pop = []
    for i in range(0, 400):
        initial_pop.append(0)

    while sum(initial_pop) != 20:
        item = random.randint(0, 399)
        if initial_pop[item] == 0:
            initial_pop[item] = 1

    one_gen.append(initial_pop)
    count += 1

with open("Program2Input.txt") as file:

    for data in file:
        print(data)
    # for i in range(0, 999):
    #     sum = 0
    #     for j in range(0, len(one_gen[i]) - 1):
    #         if one_gen[i][j] == 1:
    #         #Calculate fitness. utility and weight.
    #         else:
    #             continue
    #    print(sum)








