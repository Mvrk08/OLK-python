def cal_avg(lst):
    total = 0
    for nos in lst:
        total += nos
    average = total / len(lst)
    return average

scores = [85, 90, 78, 92, 88]
print(cal_avg(scores))


def even_odd(lst):

    even =[]
    odd =[]
    for num in lst :
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd


scores = [85, 90, 78, 92, 88]
print(even_odd(scores))


def clean_duplicates(data):
    unique = []
    for num in data:
        #if num not in unique:    ## membership  operator
        #      unique.append(num)
        if num not in unique:
            unique.append(num)
    return unique


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,22,3333,44444,44444,2,3,4,5,6,7,8]
print(clean_duplicates(numbers))



def check_palindrome(text):

    clean=text.lower()
    clean= clean.replace(",", "")

    reverse_text= clean[::-1]

    if  clean ==  reverse_text  :
        return True
    else :
        return False

print(check_palindrome("singh"))

