"""
 
 Take a year as input. Check if it is a leap year. A year is a leap
year if it is divisible by 4, but not by 100, unless it is also
divisible by 400.

 """
#
# leapyr = int(input("enter the year you want to check : "))
#
#     # if leapyr  % 4 == 0 and  leapyr % 100 != 0
#     if (leapyr % 4 == 0 and leapyr % 100 != 0) or (leapyr % 400 == 0)
#         print("leap yr got it")
#
#     else :
#         print("leap yr not detected")


leapyr = int(input("Enter the year you want to check: "))

# Fixed the logical operator to lowercase 'and'
# Added parentheses and the OR condition for years divisible by 400
# Added the missing colon (:) at the end of the if statement


if (leapyr % 4 == 0 and leapyr % 100 != 0) or (leapyr % 400 == 0):
    print("Leap year detected!")
else:
    # Fixed the indentation here to match the rest of the block
    print("Common year detected (not a leap year).")


