
# Tamim Shariar by subin

def pertition(l,low,high):
    pivot=l[high]
    i=low-1
    for j in range(low,high):
        if l[j]<pivot:
            i+=1
            l[i],l[j]=l[j],l[i]
    # swap the pivot element with the greater element specified by i
    l[i+1],l[high]=l[high],l[i+1]
    # return the position from where partition is done
    return i+1
def quick_short(l,low,high):
    if low>=high:
        return
    p=pertition(l,low,high)
    quick_short(l,low,p-1)
    quick_short(l,p+1,high)


if __name__=="__main__":
    list=[6,3,8,4,7,5]
    print(pertition(list,0,len(list)-1))
    quick_short(list,0,len(list)-1)
    print(list)

