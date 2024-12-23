#Topic : BASIC PYTHON
#Exercise Number : 28
##PROBLEM STATEMENT:
#  Write a Python code to parse the given json_exercise.json.
#  Parse the json file and print the tags list from the json.
# Python Version : 3.7
"""
 - Add the below friend (in friends key) in given json and update the existing json file
        id = 1, name = "Faye Adams"
Use : "json_exercise.json" from files folder.
"""
import json
with open('json_exercise.json') as json_file:
    data = json.load(json_file)
    print("Type:", type(data))
    print(data["tags"])
    print(data["friends"][0])
    friend_key = {'id': '1', 'name': 'Faye Adams'}
    data['friends'] = friend_key
    print(data["friends"])