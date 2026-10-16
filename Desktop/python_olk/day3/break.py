"""
Take numbers as input from the user one by one. Skip negative
numbers and keep adding the positive ones. Stop when the user
enters 0 and print the total. (Uses both continue and break.)
"""


## print 1 to 5
## i==5 break

#
# i=1
# while i<= 10 :
#     if i==5 :
#         break
#     print(i,end = " ")
#     i+=1

total =0
while True :
     num = int(input("enter the digit :  "))
     if num<=0 :
       continue

      if num==0 :
      break
      total=+1


  print(total)
