
import csv

# data_list = []

with open("D:/GitHub/python_/.csv/csv_file.py", mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        print(row)
        # name = row[0]
#         # age = row[1]  # Assuming age is an integer in the CSV
#         data_dict = [{"Name": 'ritu', "Age": 18},{"Name": 'risu', "Age": 15}, {"Name": 'ridu', "Age": 13}]
#         data_list.append(data_dict)
# print(data_list)
