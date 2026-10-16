"""
Take the user
'
s age as input. Check and print whether they are eligible
to vote (age >= 18) and whether they are a senior citizen (age >= 60).
Print both results
"""


age_checker = int(input("enter your age please :   "))

if age_checker >=60 :
    print("voter  found sr citizen")

elif age_checker >=18 :
    print (" votiing citizen")