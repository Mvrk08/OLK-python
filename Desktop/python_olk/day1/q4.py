"""
A student scored marks in 3 subjects. Take all three as input,
calculate the total and average, and print both using an f-string
"""


## 3 subjects : maths , pyhsics ,chemsitry

marks1 = int (input("enter your marks in  maths :  "))
marks2 = int (input("enter your marks in  physics :  "))
marks3 = int (input("enter your marks in   chemsitry :  "))


print(f" average of all three subjects is: {(marks1+marks2+marks3)/3} ")
print(f"total marks are like this: {marks1+ marks2+marks3 }")