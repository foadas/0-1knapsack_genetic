import csv
import math
import random

values = []
all_fitnesses = []
answers = []
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

    if total_weight > 220 or total_size > 2.0:
        fitness = 0
    else:
        fitness = total_value
    return fitness

def fitness(chromosome, object1):
    total_value = 0
    total_weight = 0
    total_size = 0.0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_value += int(object1[i][2])
            total_size += float(object1[i][1])
            total_weight += int(object1[i][0])

    fitnesss = round(total_value - (abs(220 - total_weight)) + (abs(2.0 - total_size)))
    return fitnesss

def check_population(pop, population):
    if pop in population:
        return True
    return False
def population(objects):
    i = 0
    population = []
    random.shuffle(objects)
    while (i < 200):
        total_weight = 0
        total_size = 0.0
        j = 0
        chromosome = []
        while (j < len(objects)):
            take = random.randint(0, 1)
            if take == 1:
                if (total_weight + int(objects[j][0]) <= 220 and total_size + float(objects[j][1]) <= 2.0):
                    total_weight += int(objects[j][0])
                    total_size += float(objects[j][1])
                    chromosome.append(take)
                else:
                    chromosome.append(0)
            else:
                chromosome.append(0)

            j += 1
        if not check_population(chromosome, population):
            population.append(chromosome)
            value = knapsack_fitness(chromosome, objects)
            values.append({'gen': chromosome, 'value': value})
            i += 1

    return population

def mutation(child):
    n = random.randint(24, 28)
    child[n] = 1 - child[n]
    return child

def selection(chrom_dict, sum_fitnesses):
    random_select = random.randint(1, sum_fitnesses)
    wheel = 0
    while wheel < random_select:
        for item in chrom_dict:
            if wheel + item['value'] >= random_select:
                return item['gen']
            wheel += item['value']

def crossover(population, objects2):
    children = []
    sum_of_values = sum(item['value'] for item in population)
    for k in range(0, len(population)):
        break_p = random.randint(0, len(population))
        first_chromosome = selection(population, sum_of_values)
        seceond_chromosme = selection(population, sum_of_values)
        if k == len(population)-1:
            break
        child = first_chromosome[:break_p] + seceond_chromosme[break_p:]
        # child2 = population[k+1]['gen'][break_p:] + population[k]['gen'][:break_p]
        # children.append(child1)
        value = fitness(child, objects2)
        # value2 = fitness(child2, objects2)
        if(random.randint(0,10)> 5):
            mutated_child = mutation(child)
            mutated_value = fitness(mutated_child, objects2)
            val = knapsack_fitness(mutated_child, objects2)
            answers.append({'gen': mutated_child, 'value': val})
            children.append({'gen': mutated_child, 'value': mutated_value})
        answers.append({'gen': child, 'value': knapsack_fitness(child, objects2)})
        # answers.append({'gen': child2, 'value': knapsack_fitness(child2, objects2)})
        children.append({'gen': child, 'value': value})
        # children.append({'gen': child2, 'value': value})
    return children


if __name__ == '__main__':
    objects = read_csv()
    max_weight = 220
    max_size = 2
    population = population(objects)
    sorted_list = sorted(values, key=lambda x: x["value"], reverse=True)
    i = 0
    print(sorted_list)
    answers.append(sorted_list[0])
   # maxx = sorted_list[0]['value']
    while i < 300:
        sorted_list = crossover(sorted_list, objects)
        sorted_list = sorted_list[-200:]
        sorted_list = sorted(sorted_list, key=lambda x: x["value"], reverse=True)
       # if (sorted_list[0]['value'] > maxx):
       #     maxx = sorted_list[0]['value']
        i += 1
    answers = sorted(answers, key=lambda x: x["value"], reverse=True)
    print(answers[0])