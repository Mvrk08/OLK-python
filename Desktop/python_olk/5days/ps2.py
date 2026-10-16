"""
Q51, Q80, Q93	Q53, Q81, Q99	Q57, Q104
"""

### 51


def marks_analysis(ans):
    print(max(ans))
    print(min(ans))
    average= sum(ans)/len(ans)
    return average


marks =[5, 88, 62, 91, 70, 83]

print(marks_analysis(marks))




#### 80


def  access_notfound(nope):


for subject, score in len(nope):
    if  subject ==["Maths","English","Science","History","Computer"]  :
        return True
    else :
        return False



marks = {
    "Maths": 88,
    "English": 75,
    "Science": 92,
    "History": 81,
    "Computer": 95
}

print(access_notfound(marks))





## 93

daw =input(str("enter the name please: "))
print(daw[0])
print(daw[-1])
print(len(daw))



##  53

def max_no(lst):
    for no in nos(0, n - 1):
        if no[i] < no[i + 1]
            no += nos
            return lst

nos =[1,3,55,667,88,53,22]
print(max_no(nos))

#####  81

products = {
    "Laptop": 55000,
    "Phone": 25000,
    "Headphones": 2000,
    "Keyboard": 1500
}

for prod ,value in products.items():
    if prod == product:
    print("you got it")
    print(f"price of the {prod}: {value}")
    break
else :
    print("not found")



    """
    products = {
    "Laptop": 55000,
    "Phone": 25000,
    "Headphones": 2000,
    "Keyboard": 1500
}

search = input("Enter the product you want: ")

for prod, value in products.items():
    if prod == search:
        print("You got it")
        print(f"Price of the {prod}: {value}")
        break
else:
    print("Not found")"""

######## q99

def check_first_letter(first):
    first=new.split()
    for first in new :
        if first[i]== "aeiouAEIOU" :
            return first


new =input(str("enter the sentence mfs: "))
print(check_first_letter(new))





