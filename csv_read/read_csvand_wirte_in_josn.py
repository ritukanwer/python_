import csv
import json

def read_csv_and_add_size(csv_file_path, json_file_path):
    data_list = []

    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            row['size'] = len(row['industry_name_ANZSIC'])
            data_list.append(row)
    return len(data_list)

    with open(json_file_path, mode='w') as json_file:
        json.dump(data_list, json_file, indent=2)

    print(f"Data processed and saved in JSON: {json_file_path}")

csv_file_path = "D:/GitHub/python_/.csv/anuual_enterpirse_survey.csv"
json_file_path = "D:/GitHub/python_/.csv/annual-output1231_json123_file.json"
x=read_csv_and_add_size(csv_file_path, json_file_path)
print(x)
# print(len(read_csv_and_add_size(csv_file_path, json_file_path)))

