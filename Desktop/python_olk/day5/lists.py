"""
Create a list of 5 of your favourite movies. Print the first, last, and middle movie from your list using both positive and negative indexing where appropriate.
"""


# Movies = ["dhunrdar" , "safed sagar", "jurrasic park", "opnehiemer" ,"f1"]
#
# print( Movies[0])
# print( Movies[1])
# print( Movies[3])
# print( Movies[-2])
# print( Movies[-4])
# print( Movies[-5])


"""
Create a list of 5 numbers (e.g., [10, 20, 30, 40, 50]). Replace the second and fourth elements of this list with the number 0 using indexing. Print the updated list"""

#
# nos = [10, 20, 30, 40, 50]
# nos[2]=0
# nos[4]=0
# print(nos)



"""
Question 51: Student Marks Analysis
Create a list of 6 hypothetical student marks (e.g., [75, 88, 62, 91, 70, 83]). Using built-in functions, print the highest mark, lowest mark, total sum of marks, and the average mark.
Format the average to two decimal places.
# Expected Output (using hypothetical marks):
# Highest Mark: 91
# Lowest Mark: 62
# Total Marks: 469
# Average Mark: 78.17
"""

#
# marks =[75, 88, 62, 91, 70, 83]
#
# print(f"highest marks is: {max(marks)}")
# print(f"lowest marks is: {min(marks)}")
# print(f"total marks is: {sum(marks)}")
# print(f"average marks is: {sum(marks)/6}")



"""Question 52: Sorted Lists
Create a list of numbers (e.g., [5, 2, 8, 1, 9, 3]). Print the list in ascending order and then in descending order using the sorted() function.
After printing, verify and print the original list to confirm it remains unchanged.
# Expected Output (using hypothetical list):
# Ascending Order: [1, 2, 3, 5, 8, 9]
# Descending Order: [9, 8, 5, 3, 2, 1]
# Original List: [5, 2, 8, 1, 9, 3]

"""


nos =[5, 2, 8, 1, 9, 3]
print(f"Ascending order is: {sorted(nos)}")
print(f"Descending order is: {sorted(nos, reverse=True )}")
print(f"prignal lists is : {nos}")







