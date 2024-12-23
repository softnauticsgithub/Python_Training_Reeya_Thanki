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
def get_values(input_dic,key):
    '''
    here i define function called fun to fetch the key value
    '''
    for k,value in input_dic.items():
        if k==key:
            return value
        elif type(value)==dict:
             f=get_values(value,key)
             if f is not None:
                return f
input_dict = {"k1": "v1",
             "k2": {"k3": "v3"},
             "k4": {"k5": {"k6": "v6"}}
             }
key=input()
print(get_values(input_dict,key))

# keys=["k1","k2","k3","k4","k5","k6"]
# current=input_dict
# for key in keys:
#     current=current.get(key,{})
# print(current)
# key=input()
# x=input_dict[key]
# print(x)
