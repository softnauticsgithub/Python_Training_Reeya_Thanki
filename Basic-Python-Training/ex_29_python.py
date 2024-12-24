#Topic : BASIC PYTHON
#Exercise Number : 29
##PROBLEM STATEMENT:
# Write a Python code to check if given dummy API is responding correctly?
# if API is responding with  employee's data then
# print the employee's name, age and salary whose salary is 400000.
# Python Version : 3.7
"""
- If API is not responding then display the appropriate user message.
	NOTE : Use "Requests" python module to access API.
Link to demo API : https://reqres.in/api/users?page=2
"""
import requests
response = requests.get("https://reqres.in/api/users?page=2")
if response.status_code == 200:
    response_data = response.json()
    for i in response_data['data']:
        if i['last_name'].startswith('F'):
            print("First Name : ",i['first_name'])
            print("Last Name : ",i['last_name'])
            print("Email : ",i['email'])
else:
    print("Api is not working Properly")
