#Topic : BASIC PYTHON
#Exercise Number : 31
##PROBLEM STATEMENT:
# Write a python code to convert json file to csv file.
# Python Version : 3.7
"""
USE json file created in previous exercise. 
Exercise_30
"""
import json
import csv
with open("file.json","r") as json_file:
    json_data=json.load(json_file)
data_file = open('my_csv.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
count=0
for data in json_data:
    if count == 0:
        header= data.keys()
        csv_writer.writerow(header)
        count+=1
    csv_writer.writerow(data.values())
data_file.close()
