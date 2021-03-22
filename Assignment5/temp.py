import json  # import json for adding data to text file in json format
import sys  # import for command line argument
import random  # import random to generate random number
import time  # import time for 10s sleep
import datetime  # import to get date and time

data = {"sensor": []}  # declare a dictionary

''' global function to define error count'''


# def global_var():
#     error_count = 0
tmp_alarm_count = 0
tmp_error_count = 0
hum_alarm_count = 0
hum_error_count = 0
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
             temp, temp, temp, temp, error_temp, error_temp1, 999]

    ## random value generator with 10% error rate
    error_val = random.choice(value)
    return error_val


''' Returns sensor data dictionary'''


def sensor_param(number):
    
    temperature = error_gen(40)

    if temperature == 999:
        global tmp_error_count
        tmp_error_count = tmp_error_count + 1
    else:
        if 35 > temperature or 45 < temperature:
            global tmp_alarm_count
            tmp_alarm_count = tmp_alarm_count + 1
    now = datetime.datetime.now()
    
    date_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    humidity = error_gen(40)
    
    if humidity == 999:
        global hum_error_count
        hum_error_count = hum_error_count + 1
    else:
        if 35 > temperature or 45 < temperature:
            global hum_alarm_count
            hum_alarm_count = hum_alarm_count + 1
    
    ## sensnor data
    
    data1 = {
        "id": number,
        "temperature": temperature,
        "humidity": humidity,
        "time": date_string,
        "tmp_alarm_count": tmp_alarm_count,
        "tmp_error_count": tmp_error_count,
        "hum_alarm_count": hum_alarm_count,
        "hum_error_count": hum_error_count
    }

    return data1


''' main function running infinite loop '''

# if __name__ == "__main__":
#     #global_var()
#     tmp_alarm_count = 0
#     tmp_error_count = 0
#     hum_alarm_count = 0
#     hum_error_count = 0
#     #filename = "sensor_" + sys.argv[1] + ".txt"
#     # print(filename)
#     #id = int(sys.argv[1])
#     while True:
#         time.sleep(10)
#         for x in range(3):
#             all_data = sensor_param(x)
#             print(all_data)
#         #cappend_data(sensor_param(id, temp), filename)
