# Assignment 1
This assignment generates pseudo temperature data and appends data to a txt file in json format which then is turn is read by main program to process the data and appending to another file in json format.

## Files in the project
[main.py](https://github.com/anpr9067/EID_Projects/blob/main/Assignment1/main.py) -This python file reads all txt files and writes in the etxt file in [master_log](https://github.com/anpr9067/EID_Projects/tree/main/Assignment1/master_log) as a [main_data.txt](https://github.com/anpr9067/EID_Projects/blob/main/Assignment1/master_log/main_data.txt) file.

[temp.py](https://github.com/anpr9067/EID_Projects/blob/main/Assignment1/temp.py) - This python file takes sensor id and temperature as command line argument, generates sensor_"sensor_id".txt file and appends pseudo generated sensor data to the created file.
