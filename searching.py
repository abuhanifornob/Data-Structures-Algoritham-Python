

def linear_search(number_list,find_to_number):
    for index,number in enumerate(number_list):
        if number==find_to_number:
            return index
    return -1
def binary_search(number_lists,find_to_number):
    left=0
    right=len(number_lists)-1

    while left<=right:
        mid_index=(left+right)//2
        if number_lists[mid_index]==find_to_number:
            return mid_index
        if find_to_number>number_lists[mid_index]:
            left=mid_index+1
        else:
            right=mid_index-1
    return -1
def binary_search_recursive(left,right,mid_index,linst_number,find_to_number):

    if right<left:
        return -1
    mid_index=(left+right)//2
    if linst_number[mid_index]==find_to_number:
        return mid_index
    if find_to_number>linst_number[mid_index]:
        left=mid_index+1
    else:
        right=mid_index-1
    return binary_search_recursive(left,right,mid_index,linst_number,find_to_number)




if __name__=="__main__":
    list=[7,10,12,25,30,37,42,66,96]
    find_to_number=66
    left=0
    right=len(list)-1
    mid=(left+right)//2
    index=binary_search_recursive(left,right,mid,list,find_to_number)
    print(f" Number Found at index {index} Using Linear Search ")



