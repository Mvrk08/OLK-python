"""
email validation  97
"""

# def check_email(email:str) :
#     if email.count("@") ==1  and "." in email :
#         return "valid"
#     return "invalid"
#
# input_user = input("enter the mail: ")
# print(check_email(input_user))



"""clean phone no 98
"""
#
# def clean_phone(phone):
#     phone = phone.replace("-", "")
#     phone = phone.replace("+91", "")
#     print(phone)
#
# ui=input("enter phone no: ")
# print(clean_phone(ui))
#
#
# #
# """check no of vowels 99 """



"""

Take a list of names as input (comma separated). Split them, sort them
alphabetically, and join them back with " | " as separator
"""

# def  seperation(lst):
#     lst= lst.split(",")
#     lst.sort()
#     return "|".join(lst)
#
# ui=input("enter the word: ")
# print(seperation(ui))




"""File Type Check
Take a filename as input (like report.pdf). Check if it ends with .pdf,
.docx, or .txt and print the file type.
"""
#
# def file_type(file):
#     print(file.endswith("report"))
#     print(file.endswith(".pdf"))
#     print(file.endswith(".docx"))
#
#
# ui = input("enter the file with type: ")
# file_type(ui)


def file_type(file):
    if file.endswith(".pdf"):
        print("PDF file")
    elif file.endswith(".docx"):
        print("DOCX file")
    elif file.endswith(".txt"):
        print("TXT file")
    else:
        print("Unknown file")


file = input("Enter filename: ")
file_type(file)