

"""
 Q 53-57
"""



nums = [-4,-22,-2134,4,5,6779,-1]

maxi=float("-inf")
for num in  nums :
    if  num > maxi :
        maxi=num

print(maxi)




def does_target_exists (list,target) :
    for num in list:
        if num ==target :
            return True
    return False

num =[4,5,6,66,77,321,-123]


print(does_target_exists (num,66))





def average(x):
    n = len(x)
    total = 0

    for num in x:
        total += num

    return total / n


nums = [3, 4, 5, 6, 7, 866]

print(average(nums))


#####################



def sum_of_2list(lst1,lst2):
    new_list=[]
    n=len(lst1)
    for i in range(0,n):
        total = lst1[i] + lst2[i]
        new_list.append(total)
    return new_list


nums1 =[23,3233,3242,1122]
nums2 =[3,112,3211,-22]

ans= sum_of_2list(nums1,nums2)
print(ans)

###################################
def  is_sorted(lst):
    n=len(lst)
    for i in range(0,n-1):
        if lst[i]> lst[i+1] :
            return False
    return True

nums =[2,3,4,5,6,66,77,-212,-99,444,543]

print(is_sorted(nums))




