"""
58-63
"""
##############################
def find_largest_smallest(nums):
    largest = nums[0]
    smallest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

        if num < smallest:
            smallest = num

    return largest, smallest


nums = [3, 1, 4, 1, 5]

largest, smallest = find_largest_smallest(nums)

print("Largest:", largest)
print("Smallest:", smallest)
##############################

def add_list(lst1,lst2):
    new_lst = []
    n =len(lst1)
    for i in range(0,n):
        total =lst1[i] + lst2[i]
        new_lst.append(total)
    return new_lst


no1 = [3, 1, 4, 1, 5]
no2 = [3, 4, 3, -4, 25]

ans=add_list(no1,no2)
print(ans)


##############################

def reverse_lst(lst) :
    n=len(lst)
    new_lst=[]
    for i in range(n-1,-1,-1):
        new_lst.append(lst[i])
    return new_lst


lst1 = [3,4,55,66,77,88,-9]

ans =reverse_lst(lst1)
print(ans)


##############


def remove_dup(lst) :

  result = []
  for num in lst :
      if num not in result :
        result.append(num)
  return result


nums = [12,2,2,3,3,3,4,5,5,6,677 ,677]
print(remove_dup(nums))




##################################

"""
even , odd no 
"""
def check_oddeven(lst:




nos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]