# import csv
# import json
#
# def read_csv_and_add_size(csv_file_path, json_file_path):
#     data_list = []
#
#     with open(csv_file_path, mode='r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             row['size'] = len(row['name'])
#             data_list.append(row)
#
#     with open(json_file_path, mode='w') as json_file:
#         json.dump(data_list, json_file, indent=2)
#
#     print(f"Data processed and saved in JSON: {json_file_path}")

# csv_file_path = "D:/GitHub/python_/.csv/output_csv_file.csv"
# json_file_path = "D:/GitHub/python_/.csv/outputs_json_file.json"
# read_csv_and_add_size(csv_file_path, json_file_path)


# import csv
# import json
# from datetime import datetime
#
#
# def read_csv_and_add_size_time(csv_file_path, json_file_path):
#     data_list = []
#
#     with open(csv_file_path, mode='r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             row['size'] = len(row['name'])
#
#             row['datetime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#
#             data_list.append(row)
#
#     with open(json_file_path, mode='w') as json_file:
#         json.dump(data_list, json_file, indent=2)
#
#     print(f"Data processed and saved in JSON: {json_file_path}")
#
# csv_file_path = "D:/GitHub/python_/.csv/output_csv_file.csv"
# json_file_path = "D:/GitHub/python_/.csv/output1_json_file.json"
# read_csv_and_add_size_time(csv_file_path, json_file_path)

import csv
import json
from datetime import datetime


def read_csv_and_add_size_time(csv_file_path):
    data_list = []

    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            row['size'] = len(row['name'])

            row['datetime'] = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

            data_list.append(row)

    current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    json_file_path = f"D:/GitHub/python_/.csv/output_json_file_{current_datetime}.json"

    with open(json_file_path, mode='w') as json_file:
        json.dump(data_list, json_file, indent=2)

    print(f"Data processed and saved in JSON: {json_file_path}")

csv_file_path = "D:/GitHub/python_/.csv/output_csv_file.csv"
read_csv_and_add_size_time(csv_file_path)
