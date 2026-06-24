#Topic : BASIC PYTHON
#Exercise Number : 19
##PROBLEM STATEMENT:
#Write a Python function to check whether two given strings are anagram o
#f each other or not. Code must not contain sort or any other
# sorted inbuilt functions.
#NOTE: An anagram of a string is another string that contain
#the same characters in the same frequency,
#only the order of characters can be different. For example,
#“abcd” and “dabc” are an anagram of each other.
#Python Version : 3.7
'''Anagram String'''
from collections import Counter
def check_anagram(s1,s2):
    ''' Here I define Check Anagram Function'''
    if Counter(s1) == Counter(s2):
        print("Strings are anagram")
    else:
        print("Strings are not anagram")

s1=input()
s2=input()
check_anagram(s1,s2)
