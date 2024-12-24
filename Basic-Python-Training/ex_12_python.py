#Topic : BASIC PYTHON
#Exercise Number : 7
##PROBLEM STATEMENT:
#Find the Percentage
#Python Version : 3.7
"""
name_keys : [Values are set of marks]
Example: 
    Raj : [80,77,49]
    Yash : [60,67,69]
    Rohit : [30,67,89]
query_name = Key i.e "Rohit"
Average score for query_name = (30+67+89)/3 = 62.0
Input Constraints : 
The first line contains the integer n , the number of students' records. 
The next n lines contain the names and marks obtained by a student,
each value separated by a space.
The final line contains query_name, the name of a student to query.
        2 <= n <= 10
    # marks[i] = List of marks
        0 <= marks[i] <= 100
    # Length of marks array = 3
Required Output Format : 
    Print one line: The average of the marks obtained by the
    particular student correct to 2 decimal place.
"""
n=int(input("Enter the number of Student : "))
if n >= 2 and n <= 10 :
    student_name_and_marks={}
    for i in range(n):
        name, sub1, sub2, sub3 = input().split(" ")
        if int(sub1) >= 100 or int(sub1) <= 0:
            sub1 = input("Please Enter mark below 100 and above 0")
        if int(sub2) >= 100 or int(sub2) <= 0:
            sub2 = input("Please Enter mark below 100 and above 0")
        if int(sub3) >= 100 or int(sub3) <= 0:
            sub3 = input("Please Enter mark below 100 and above 0")
        s1 = int(sub1)
        s2 = int(sub2)
        s3 = int(sub3)
        student_name_and_marks[name] = list([s1, s2, s3])
        print(student_name_and_marks)
    name = input("Enter the name of the student ")
    for i,j in student_name_and_marks.items():
        if name in i:
            percent = sum(j) * 100 / 300
            print(percent)
            break
    else :
        print("Name is not Found!!")
else:
    print("Please enter the number in range of 2 to 10")
