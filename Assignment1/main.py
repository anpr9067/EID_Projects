# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import time
import json
import datetime

process_data = {"processed data": []}
filename = "master_log/main_data.txt"


''' function that processes data '''

def read_file(data, len):
    if len == 0:
        data_main = {}
        return data_main
    elif len < 10:
        minrange = -len
    else:
        minrange = -10

    avg = 0
    count = 0
    if data[-1]["temperature"] != 'NA':
        min = data[-1]["temperature"]
        max = data[-1]["temperature"]
    sensor_id = data[-1]["id"]
    error_count = data[-1]["error count"]
    alarm_count = data[-1]["alarm count"]

    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%Y %H:%M:%S")

    for x in range(minrange, 0):
        if data[x]["temperature"] != 'NA':
            avg += data[x]["temperature"]
            count = count + 1
            if float(data[x]["temperature"]) < min:
                min = data[x]["temperature"]
            if float(data[x]["temperature"]) > max:
                max = data[x]["temperature"]

    if count == 0:
        avg = 0
    else:
        avg = avg / count
    ## processed data
    data_main = {
        "id": sensor_id,
        "timestamp": date_string,
        "temperature high": max,
        "temperature low": min,
        "temperature average": avg,
        "error count": error_count,
        "alarm_count": alarm_count
    }

    return data_main

''' open sensor file '''


def open_files():
    for f in os.listdir("./"):
        if f.endswith(".txt"):
            try:
                file = open(f, "r")
                data = json.load(file)
                sensor_data = data["sensor"]
                length = len(sensor_data)
                append_data(read_file(sensor_data, length), filename)
            except IOError:
                print("Error: File does not appear to exist.")
            finally:
                file.close()

''' write processed data into file'''

def append_data(data1, filename):
    try:
        with open(filename) as file:
            data = json.load(file)
            temp = data["processed data"]
            temp.append(data1)

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    except IOError:
        print("Error opening file");

    finally:
        file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    with open(filename, 'a') as file:
        json.dump(process_data, file, indent=4)

    while True:
        open_files()
        time.sleep(30)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
