import csv

def read_csv():
    file_path = 'backpack_objects.csv'
    objects = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            objects.append(row)
    return objects


if __name__ == '__main__':
    objects = read_csv()
    
