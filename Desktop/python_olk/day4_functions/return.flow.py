"""
return  true if prime othwewise not
"""


def check_prime(num):

    count=0
    for i in range (1, num+1):
        if num%i==0:
            count+=1

    if count==2:
        return True
    return False

print(check_prime(23))