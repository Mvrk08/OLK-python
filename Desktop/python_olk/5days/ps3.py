"""
Day 3 — 9 questions
🟢 Q52 — Sorted Lists
🟢 Q82 — World Capitals
🟡 Q56 — Element-wise Sum
🟡 Q83 — Subject Performance Analysis
🟡 Q100 — Sorted Names
🔴 Q58 — Largest and Smallest
🔴 Q102 — Longest Word
🔴 Q110 — Most Common Word
"""

#######  q52

######## q 82

capitals = {
    "India": "New Delhi",
    "France": "Paris",
    "Japan": "Tokyo",
    "Italy": "Rome",
    "Australia": "Canberra"
}
for Country  in  capitals.keys():
     print (f" {Country}-->   {capitals[Country]}")


#########   q56


#
# def add_2lsts(new_lst):
#     new_lst= len(list1)
#     new_lst = len(list2)
#      for i in  list2:
#         list1.append(i)
#      return.append()
#
# list1 = [10, 20, 30, 40]
# list2 = [1, 2, 3, 4]
#
# print(add_2lsts(new_lst))




#########   q83


marks = {
    "Maths": 85,
    "Science": 90,
    "English": 78,
    "Computer": 95,
    "Punjabi": 82
}

total=0
avg=0
for subject in marks.values():
    total += subject
    avg = sum(marks.values())/len(marks.values())
    break

print(f"total marks is :{total}")
print(f"avg is like :{avg}")



######### q 100

names= input(str("enter the names: "))

new=names.split()
new=names.list(names)
print(new)




######## q58

def max_min(sum):
    sum =len(list)
    for i in sum():
        if


list = [10, 20, 30, 40]




########## q102









