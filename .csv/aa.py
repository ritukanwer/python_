
# WRITE_CSV_FILE
import json
import datetime

current_datetime = datetime.datetime.now()
current_datetime_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

data = [{
    'name': 'ritu',
    'age': 25,
    'city': 'jaipur',
    'date':current_datetime_str

    },
    {
    'name': 'rishi',
    'age': 25,
    'city': 'jaipur',
    'date':current_datetime_str


    },
    {
    'name': 'rina',
    'age': 25,
    'city': 'jaipur',
    'date':current_datetime_str
}]
for i in data:
    print(i)
    with open("D:/GitHub/python_/.csv/.csv", 'w', newline='') as json_file:
        json.dump(data, json_file)

print(json.dumps(data))
