
## 3 ints as total
#
# def addition(a,b,c) :
#     ans = a+b+c
#     print(f"total= {ans}")
#
# addition(10,22,3)


## ask name, age ,gender as input :

#
# def greet(name, age , gender) :
#     print(f"salam {name} apki  {age} saal ke hai aur aap {gender} hai")
#
# n=str(input("your name: "))
# a=int(input("your age: "))
# b=str(input("your gender: "))
#
# greet(n,a,b)



"""
function to create area of rectangle
"""


# def rect(length, brd):
#      area =length * brd
#      print(f"you value is : {area}")
#
# rect(10,20)



"""
Write a function called find_max that takes three numbers as
parameters and prints the largest one.  q39
"""

# def find_max(n1,n2,n3):
#     if n1 > n2 and n1 > n3:
#         Result = "n1 is greatest"
#
#     elif n2 > n3 and n2 > n1:
#         Result = "n2 is greatest"
#
#     else:
#         Result = " n3 is greatest"
#
#     print(Result)
#
# find_max(22, 3, 445






"""
 Write a function called discount_price that takes original_price
and discount_percent as parameters and prints the final
price after discount.

"""

#
def  discount_price (original_price , discount_percent) :
  dic_amt = (discount_percent/100) * original_price
  final_amount =original_price-dic_amt
  print(f'here you go{ : final_amount}')

discount_price (100,50)


