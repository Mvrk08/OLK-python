"""
Day 1 — 8 questions
🟢 Q49 — Favourite Movies -- done already
🟢 Q50 — Number Replacement
🟢 Q79 — Student Profile
🟡 Q55 — Calculate Average
🟡 Q62 — Separate Even/Odd
🟡 Q97 — Email Validation
🔴 Q61 — Remove Duplicates
🔴 Q105 — Palindrome Check
"""


####### q55

def cal_avg(lst):
    total = 0
    for nos in lst[i]:
        total += nos
    average = total / len(lst)
    return average

scores = [85, 90, 78, 92, 88]
print(cal_avg(scores))



####### q62


def even_odd(numbers):
    even = []
    odd= []
    for num in numbers :
        # if i %2==0
        #     return lst1.append()
        # else :
        #     return lst2.append()
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_odd(numbers))



######## q97

io=input("Enter you email:")
email =" "
for index in email() :
    if email[index]== "@" and email [index]== "." :
     print("valid")
    else :
        print("invalid")





########## q61

#
# def clean_duplicates (lst1):
#     lst1 =data.copy()
#     for ls1 in range():
#         lst1.append()
#         return lst1
#
#
# data = [10, 20, 30, 20, 10, 40, 50, 40]
# print(clean_duplicate(data))




def clean_duplicates(data):
    unique =[]
    for num in data :
       """if num not in unique:    ## membership  operator
            unique.append(num)"""
        if num not in unique :
            unique.append(num)

        return  unique

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(clean_duplicates(numbers))



########## q105


def is_palindrome(text):

   cleaned =text.lower()
   cleaned=cleaned.replace(" ", "")

    # reverse_text= text[::-1]
   reverse_text = cleaned[::-1]

    if cleaned == reverse_text :
        return True
   else:
        return False


print(is_palindrome("Race car"))  # Expected: True
print(is_palindrome("hello"))     # Expected: False
print(is_palindrome("Level"))     # Expected: True


