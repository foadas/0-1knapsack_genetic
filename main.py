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

def knapsack_fitness(chromosome, object):
    total_value = 0
    total_weight = 0
    total_size = 0.0

    for i in range(len(chromosome)):
        if chromosome[i] == 1: 
            total_value += int(object[i][2])
            total_size += float(object[i][1])
            total_weight += int(object[i][0])

    if total_weight > 220 and total_size > 2.0:
        fitness = 0
    else:
        fitness = total_value
    return fitness


def population(objects):
    i = 0
    population = []
    while(i<200):
        total_weight = 0
        total_size = 0.0
        j = 0
        selections = []
        while(j<len(objects)):
            take = random.randrange(2)
            if take == 1:
                if(total_weight + int(objects[j][0])<=220 and total_size + float(objects[j][1])<=2.0):
                    total_weight += int(objects[j][0])
                    total_size += float(objects[j][1])
                    selections.append(take)
                else:
                    selections.append(0)
            else:
                selections.append(0)
                
            j+=1
        population.append(selections)
        value = knapsack_fitness(selections, objects)
        values.append(value)
        i+=1

def crossover():
    
    


if __name__ == '__main__':
    objects = read_csv()
    max_weight = 220
    max_size = 2
    population = population(objects)
    
    

