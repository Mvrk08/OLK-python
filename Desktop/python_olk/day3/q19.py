"""
Q19. Ask a number from the user, and print all the factors.
"""

num =int(input("enter the no :  "))
i=1
count =0
while i<=num :
   if  num % i==0 :
       count= count+ 1
    print(i)
   i+=1
