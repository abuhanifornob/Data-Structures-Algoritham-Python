# When i try to find number 5 in below list using binary search it dosn't work and return me -1 index
# Why is that?
                # numbers=[1,4,6,9,10,5,7]

#2.


############ BINARY SEARCH EXERCISE SOLUTION: CODEBASICS YOUTUBE CHANNEL ####################

################### PROBLEM 1 #######################
#  When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?
#  numbers = [1,4,6,9,10,5,7]
#  Answer: It is because the list is not sorted! Binary search requires that list has to be sorted

################### PROBLEM 2 #######################
# Problem: Find index of all the occurances of a number from sorted list
# Solution here tries to find an index of a number using binary search. Now since the list is sorted,
# it can do left and right scan from the initial index to find all occurances of a given element
# This method is not most efficient and I want you to figure out even a better way of doing it. In
# any case below method is still effective

def binary_search(number_lists,find_to_number):
    left=0
    right=len(number_lists)-1
    while left<=right:
        mid_index=(left+right)//2
        if find_to_number==number_lists[mid_index]:
            return mid_index
        if number_lists[mid_index]<find_to_number:
            left=mid_index+1
        else:
            right=mid_index-1
    return -1

def all_the_ocurrence(list,find_to_number):
    index=binary_search(list,find_to_number)
    include=[index]
    i=index-1
    while i>=0:
        if list[i]==find_to_number:
            include.append(i)
        i-=1
    i=index+1
    while i< len(list):
        if list[i]==find_to_number:
            include.append(i)

        i+=1

    return sorted(include)



if __name__=="__main__":
    numbers = [1,4,6,15,9,11,15,15,15,17,21,34,34,56]
    find_to_number=15
    index=binary_search(numbers,find_to_number)
    print(f" Number Found at {index} use Binary Search ")
    print("Print the all occunt",all_the_ocurrence(numbers,find_to_number))