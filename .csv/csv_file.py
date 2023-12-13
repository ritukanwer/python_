import csv
list = []
with open("D:/GitHub/python_\/.csv/csv_file.py", mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)