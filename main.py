import csv
import random

def read_csv():
    file_path = 'backpack_objects.csv'
    objects = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            objects.append(row)
    return objects

def population(objects):
    i = 0
    population = []
    while(i<200):
        j = 0
        selections = []
        while(j<len(objects)):
            selections.append(random.randrange(2))
            j+=1
        population.append(selections)
        i+=1

    print(population)

if __name__ == '__main__':
    objects = read_csv()
    population = population(objects)

    
