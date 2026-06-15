#Topic : BASIC PYTHON
#Exercise Number : 30
##PROBLEM STATEMENT:
# Write a Python code to convert the given csv file to some json file
# Python Version : 3.7
"""
USE : python_exercise.csv from files folder.
   Note: Output json file will be like 
        {"1": 
            {
                "Company": Tata
                "Car Model": Punch
            }
            ...
        }
    once output json file is generated add few more enetries
    manually in the json file and pefrom the next exercise.
"""
import csv
import json
csv_file = open('python_exercise.csv', 'r')
json_file = open('file.json', 'w')
field_names = ("No","Company","Car Model")
reader = csv.DictReader( csv_file, field_names)
out_file = json.dumps( [ row for row in reader ] )
json_file.write(out_file)
csv_file.close()
json_file.close()
