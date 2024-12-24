#Topic : BASIC PYTHON
#Exercise Number : 33
##PROBLEM STATEMENT:
# Convert below xml string to the json file, generate the json file at given location.
# Python Version : 3.7
"""
  xml_str = '''
        <cars>
            <car type="A" value="32"/>
            <car type="B" value="42"/>
            <car type="C" value="55"/>
            <car type="D" value="23"/>
        </cars>
    '''
    Output json file will contain as below
    { 'A': 32, 'B': 42, 'C': 55, 'D': 23 }
    NOTE: Use ElementTree for XML data handling
"""
import xml.etree.ElementTree as E
import json
XML_STR = '''
        <cars>
            <car type="A" value="32"/>
            <car type="B" value="42"/>
            <car type="C" value="55"/>
            <car type="D" value="23"/>
        </cars>
    '''
root=E.fromstring(XML_STR)
cars={}
for a in root.findall('car'):
    car_type=a.get('type')
    car_value=int(a.get('value'))
    cars[car_type]=car_value
print(cars)
json_data=json.dumps(cars)
print(json_data)
with open("ex_33_json.json",'w') as json_file:
    json_file.write(json_data)
