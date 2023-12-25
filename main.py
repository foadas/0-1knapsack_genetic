import csv
import random

values = []


def read_csv():
    file_path = 'backpack_objects.csv'
    objects = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            objects.append(row)
    return objects


def knapsack_fitness(chromosome, object1):
    total_value = 0
    total_weight = 0
    total_size = 0.0

    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_value += int(object1[i][2])
            total_size += float(object1[i][1])
            total_weight += int(object1[i][0])

    if total_weight > 220 and total_size > 2.0:
        fitness = 0
    else:
        fitness = total_value
    return fitness


def population(objects):
    i = 0
    population = []
    while (i < 200):
        total_weight = 0
        total_size = 0.0
        j = 0
        selections = []
        while (j < len(objects)):
            take = random.randrange(2)
            if take == 1:
                if (total_weight + int(objects[j][0]) <= 220 and total_size + float(objects[j][1]) <= 2.0):
                    total_weight += int(objects[j][0])
                    total_size += float(objects[j][1])
                    selections.append(take)
                else:
                    selections.append(0)
            else:
                selections.append(0)

            j += 1
        population.append(selections)
        value = knapsack_fitness(selections, objects)
        values.append({'gen': selections, 'value': value})
        i += 1
    return population

def mutation(child):
    n = random.randint(20, 26)
    child[n] = random.randrange(2)
    return child


def crossover(population, objects):
    children = []
    for k in range(0, 200, 2):
        child = population[k]['gen'][:(29 // 2)] + population[k + 1]['gen'][(29 // 2):]
        children.append(child)
        value = knapsack_fitness(child, objects)
        if(random.randint(0,10)> 5):
            mutated_child = mutation(child)
            mutated_value = knapsack_fitness(mutated_child, objects)
            population.append({'gen': mutated_child, 'value': mutated_value})

        population.append({'gen': child, 'value': value})

    return population


if __name__ == '__main__':
    objects = read_csv()
    max_weight = 220
    max_size = 2
    population = population(objects)
    sorted_list = sorted(values, key=lambda x: x["value"], reverse=True)
    i = 0
    print(sorted_list[0])
    maxx = sorted_list[0]['value']
    while i < 300:
        sorted_list = crossover(sorted_list, objects)
        sorted_list = sorted(sorted_list, key=lambda x: x["value"], reverse=True)
        if (sorted_list[0]['value'] > maxx):
            maxx = sorted_list[0]['value']

        i += 1
    print(sorted_list[0]['value'])
    print(maxx)



