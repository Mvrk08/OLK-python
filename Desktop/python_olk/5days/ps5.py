"""
#### Day 5 — 9 questions

🟢 Q60 — Merge Two Lists

🟢 Q95 — Count Vowels

🟢 Q96 — Alternate Characters

🟡 Q65 — Replace Negative Numbers

🟡 Q101 — File Type Check

🟡 Q103 — Username Validation

🔴 Q108 — Capitalize Long Words

🔴 Q109 — PAN Card Validation

🔴 Q106 — Word Lengths
"""



######## 60
def addlst(lst1,lst2):
    new = []
    new.extend(lst1)
    new.extend(lst2)

lst1 = list(map(int, input("Enter first list numbers separated by spaces: ").split()))

lst2 = list(map(int, input("Enter second list numbers separated by spaces: ").split()))

result = addlst(lst1, lst2)

print("Merged list:", result)


#######   95



def count_vowels(text):
    text=text.lower()
    vowels="aeiouw"
    count=0

    for i in text :
        if i in vowels :
            count+=1
    return count

sentence = input("Enter a sentence: ")
print("Total vowels:", count_vowels(sentence))


#######   96


#########   65


def replace_negative(nums):
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = 0

    return nums


result = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(replace_negative(result))



######### 103

def check_username(user):
    user=user.strip()

    if user and user[0].isalpha():
        return "Valid"
    else:
        return "Invalid"


username = input("Enter username: ")
print(check_username(username))




########### 108

def first_letter(txt):







