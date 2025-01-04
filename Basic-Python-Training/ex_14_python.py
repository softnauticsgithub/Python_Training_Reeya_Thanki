#Topic : BASIC PYTHON
#Exercise Number : 14
##PROBLEM STATEMENT:
#Write a Python code to print the value of given key from the dictionary.
# Python Version : 3.7
"""
 Code must need to handle the test case where key can be present at any inner nested dictionary.
    Example:
        input_dict = {"k1": "v1",
             "k2": {"k3": "v3"},
             "k4": {"k5": {"k6": "v6"}}
             }
    Sample Input1: k6
    Sample Output1: v6
    Sample Input2: k1
    Sample Output2: v1
    Sample Input3: k4
    Sample Output3: {"k5": {"k6": "v6"}
"""
input_dict1 = {"k1": "v1",
             "k2": {"k3": "v3"},
             "k4": {"k5": {"k6": "v6"}}
             }

temporary_dict = {}
def recursive_dict(input_dict):
    """ This function will recursively check for the available dictionaries at the place of values
    inside the given dictionary.

        args :- dictionary containing nested dictionaries as their values.
        return :- dictionary that contains all nested dictionaries separately.
    """
    for key, value in input_dict.items():
        temporary_dict[key] = value
        if isinstance(value, dict):
            recursive_dict(input_dict[key])
    return temporary_dict

final_dict = recursive_dict(input_dict1)
try:
    keys = input("Enter the key : ")
    print(keys,":",final_dict[keys])
except KeyError:
    print("Invalid Key...")


