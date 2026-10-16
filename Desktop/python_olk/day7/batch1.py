
"""
Take a name as input from the user. Print its first character, its last
character, and the total length of the name.
"""

def details(name):
     print("1st char", name[0])
     print("2ndt char" ,name[1])
     print("full char" ,len(name))

name =input("enter the characters: ")
details(name)



"""
reverse a string
"""


def reverse(text):
    return text [:: -1]

user_input= input("enter the sentence: ")
print(reverse(user_input))


"""
Read a sentence from the user. Count and print the total number of
vowels (a, e, i, o, u, case-insensitive) present in it, using a for loop
"""



def check_vowel(vowels):
    # def check_vowel(word):
    #     for i in range(len(word)):
    #         if word[i] in "aeiouAEIOU":
    for char in  vowels :
        if char=="aeiouAEIOU" :
            return True

    return False

user=input("enter the character: ")
print(check_vowel(user))




"""Given a string input, print every alternate character starting from the
very first character, using string slicing.

"""


def alternate_nos(s):
    return s[::-2]


word =input("enter the word: ")
print(alternate_nos(word))

