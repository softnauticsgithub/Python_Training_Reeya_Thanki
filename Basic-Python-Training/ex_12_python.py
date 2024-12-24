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
number_of_student = int(input("Enter the number of student in range of 2 to 10 "))
student_name_marks={}
for i in range(number_of_student):
    name,sub1,sub2,sub3=input("Enter the name and marks sperated by space ").split(" ")
    if int(sub1)>100 or int(sub1)<0:
        sub1=input("renter subject1 mark correctly ")
    if int(sub2) > 100 or int(sub2) < 0:
        sub1 = input("renter subject1 mark correctly ")
    if int(sub3) > 100 or int(sub3) < 0:
        sub1 = input("renter subject1 mark correctly ")
student_name_marks[name] = list([sub1, sub2, sub3])
name_of_student = input("Enter the name of the student ")
print(student_name_marks)
student_mark = list(student_name_marks.get(name_of_student))
if student_mark:
    average_marks = (int(student_mark[0]) + int(student_mark[1]) + int(student_mark[2])) / 3
    print("average mark of %s is %0.2f" % (name_of_student, average_marks))
else:
    print("Enter student name is not correct!")
