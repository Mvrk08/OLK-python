""""
Q83: Subject Performance Analysis
Given a dictionary of marks for different subjects, loop over its values()
to calculate and print the total marks and the average mark obtained.
"""
#
# marks = {
#     "Sst": 98 , "hindi": 95,    "english": 93,  "math": 78,
#
# }
#
# total_subjects = len(marks)
# total_marks=0
#
# # print(f"average={total_marks/total_subjects}")
#
# for mark in marks.values():
#     total_marks += mark
# print(f"average={total_marks / total_subjects}")



"""Q84: Top Scorers
Populate a dictionary with six student names and their corresponding
marks. Loop through it and print the names of all students who achieved
a score above 75.
"""

#
# students = {
#     "gandu": 56,
#     "chuman": 78,
#     "ganjedi": 98,
#     "oggy": 44,
#     "hamza": 85
# }
#
# for name , marks in students.items():
#     if marks>=75 :
#         print(f"students= {name} "
#               f"marks scored = {marks}")



"""Q85: Dictionary Merge Function
Write a Python function named merge_dicts(d1, d2) that accepts two
dictionaries (d1 and d2) as arguments and returns a new dictionary
formed by merging them using the update() method. Ensure d1 remains
unchanged
"""