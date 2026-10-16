"""
Take three numbers as input. Print the largest of the three without using any
built-in function.
"""


n1= int (input("enter no1: "))
n2= int (input("enter no2: "))
n3= int (input("enter no3: "))

if (n1>n2) and(n1>n3):
    print(" 1st no is greatest")

elif (n2>n1) and (n2>n3):
    print("2nd no is the greatest")

else :
    print("3rd no is the greatest")

