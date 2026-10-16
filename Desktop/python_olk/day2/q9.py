"""
Q9: Take a student'
s marks as input. Print their grade based on this scale:
90 and above → A
75 to 89 → B
60 to 74 → C
40 to 59 → D
Below 40 → F
"""


marks =float(input("enter your marks:  "))

if marks >= 90:
    grade = 'A'
elif marks >= 75:
    grade = 'B'
elif marks >= 60:
    grade = 'C'
elif marks >= 40:
    grade = 'D'
else:
    grade = 'F'

# Print the result
print(f"Grade: {grade}")45