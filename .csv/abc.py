# READ CSV FILE
import json
import csv
from datetime import datetime
def csvfile_to_json(csv_file_path, json_file_path):
    data_list = []

    with open("D:/GitHub/python_/.csv/output_csv_file.csv", mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # data_dict ={}
        for row in csv_reader:
            row['size'] = len(row['name'])
            row['datetime'] = datetime.now().strftime("%d-%m-%Y, %H:%M:%S.%p,%A")
            data_list.append(row)
    # print(data_list)
    current_datetime = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    output_json_file = f"D:/GitHub/python_/.csv/output_json_file_{current_datetime}.json"
    with open(output_json_file, 'w') as json_file:
            json.dump(data_list, json_file, indent = 2)

    print(f"data save in json{output_json_file}")
csv_file_path = "D:/GitHub/python_/.csv/output_csv_file.csv"
json_file_path= "D:/GitHub/python_/.csv"
csvfile_to_json(csv_file_path, json_file_path)
