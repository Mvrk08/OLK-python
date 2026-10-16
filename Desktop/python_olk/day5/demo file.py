"""
Question 57: Check if a List is Sorted


Q59. Reverse a list without using the
.reverse() method or list slicing ([::-1]).
Hint: Think about swapping elements from
both ends of the list using a loop.
Example: [1, 2, 3, 4, 5] → [5, 4, 3, 2, 1]




Q60. Given two lists, merge them into a
single new list without modifying the
originals.
Hint: Use the + operator or a loop to
combine. Example: list1 = [1, 2], list2 = [3,
4] → merged = [1, 2, 3, 4]


q64
separate a list of integers into two distinct lists: one
containing all the even numbers and the other
containing all the odd numbers.
# Example input:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected output:
# evens = [2, 4, 6, 8, 10]
# odds = [1, 3, 5, 7, 9]



Question 65
Write a Python script that iterates through a list of integers and
replaces every negative number found in the list with the value 0.
# Example input list:
numbers = [5, -3, 8, -1, 0, -10, 12]
# Expected output: [5, 0, 8, 0, 0, 0, 12]

"""


#
# def sorted_lst(lst):
#     n=len(lst)
#     for i in range(0,n-1):
#         if lst[i]> lst[i+1] :
#          return False
#     return True
#
# nums =[2,3,4,5,6,66,77,-212,-99,444,543]
#
# print(sorted_lst(nums))
#
#




# def  reverse_lst(lst) :
#     new_lst= []
#     n=len(lst)
#     for i in range(n-1,-1,-1):
#         new_lst.append(lst[i])
#     return   new_lst
#
#
# nums = [2, 3, 4, 5, 6, 66, 77, -212, -99, 444, 543]
#
# print(reverse_lst(nums))




# def combine_lst(lst1,lst2) :
#     n=len(lst1)
#     new_lst=[]
#     for i in range(0,n):
#         new_lst.append(lst1[i] + lst2[i])
#     return new_lst
#
# nums1 = [2,3,4,5,6,7]
# nums2 = [2,3,4,5,6,7]
#
# print(combine_lst(nums1, nums2))



#  def even_vs_odd(lst1, lst2):
#      lst1=[]
#      lst2 =[]
#      n=len(nums)
#
#      for i in range(0,n):
#          if i%2==0 :
#              lst1.append()
#              return  odd
#
#         else :
#             return even
#
# nums = [2, 3, 4, 5, 6, 66, 77, -212, -99, 444, 543]






def even_vs_odd(lst):

    even = []
    odd = []

    n = len(lst)

    for i in range(0, n):
        if lst[i] % 2 == 0:
            even.append(lst[i])
        else:
            odd.append(lst[i])

    return even, odd


nums = [2, 3, 4, 5, 6, 66, 77, -212, -99, 444, 543]

print(even_vs_odd(nums))
