import json  # import json for adding data to text file in json format
import sys  # import for command line argument
import random  # import random to generate random number
import time  # import time for 10s sleep
import datetime  # import to get date and time

data = {"sensor": []}  # declare a dictionary

''' global function to define error count'''


def global_var():
    error_count = 0


''' returns pseudo temperature as per requirement'''


def error_gen(maintemp):
    temp_start = maintemp - 2
    temp_stop = maintemp + 2
    rand_temp = random.randint(temp_start * 100, temp_stop * 100)
    temp = rand_temp / 100
    error_temp = random.randint(maintemp - 8, maintemp - 2)
    error_temp1 = random.randint(maintemp + 2, maintemp + 8)

    value = [temp, temp, temp, temp, temp, temp, temp,
             temp, temp, temp, temp, temp, temp, temp,
             temp, temp, temp, temp, error_temp, error_temp1, None]

    ## random value generator with 10% error rate
    error_val = random.choice(value)
    return error_val


''' Returns sensor data dictionary'''


def sensor_param(number, temp):
    temperature = error_gen(temp)
    if temperature is None:
        temperature = "NA"
        global error_count
        error_count = error_count + 1
    else:
        if temp - 5 > temperature or temp + 5 < temperature:
            global alarm_count
            alarm_count = alarm_count + 1
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%Y %H:%M:%S")

    ## sensnor data
    data1 = {
        "id": number,
        "temperature": temperature,
        "time": date_string,
        "alarm count": alarm_count,
        "error count": error_count
    }
    return data1


''' appends dictionary data to text file in json format '''


def append_data(data1, filename):
    try:
        with open(filename) as file:
            data = json.load(file)
            temp = data["sensor"]
            temp.append(data1)

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    except IOError:
        print("Error opening file");

    finally:
        file.close()


''' main function running infinite loop '''

if __name__ == "__main__":
    global_var()
    alarm_count = 0
    error_count = 0
    filename = "sensor_" + sys.argv[1] + ".txt"
    # print(filename)
    id = int(sys.argv[1])
    temp = int(sys.argv[2])
    with open(filename, 'a') as file:
        json.dump(data, file, indent=4)
    file.close()

    while True:
        time.sleep(10)
        append_data(sensor_param(id, temp), filename)
