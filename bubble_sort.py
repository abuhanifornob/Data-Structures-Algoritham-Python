
def bubble_sort(number_list):
    for i in range(0,len(number_list)):
        for j in range(0,len(number_list)-1-i):
            if number_list[j]>number_list[j+1]:
                tem=number_list[j]
                number_list[j]=number_list[j+1]
                number_list[j+1]=tem


if __name__=="__main__":
    list=[-45,10,445,8,5,7,82,45,-100]
    print(f"Befor Sorting Data {list}")
    bubble_sort(list)
    print(f"After Sorting Data {list}")
