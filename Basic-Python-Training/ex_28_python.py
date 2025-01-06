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
json_file="json_exercise.json"
with open(json_file, 'r',encoding='utf-8') as jsread:
    data = json.load(jsread)
print(f"Tags:{data['tags']}")
data_insert={ "id" :1, "name" : "Faye Adams"}
data['friends'].append(data_insert)
with open(json_file,'w') as jswrite:
    json.dump(data,jswrite,indent=4)
print("The data is updated")

