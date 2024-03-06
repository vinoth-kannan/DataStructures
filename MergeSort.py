def merge_sort(numbers,l,r):
    if l<r:
        mid=(l+r)//2
        merge_sort(numbers,l,mid)
        merge_sort(numbers,mid+1,r)
        merge(numbers,l,mid,r)

def merge(numlist,l,m,r):
    n1 = m - l + 1
    n2 = r - m
    llist=[0]*n1
    rlist=[0]*n2
    finallist=[0]*(r-l+1)
    for x in range(n1):
        llist[x]=numlist[l+x]
    for y in range(n2):
        rlist[y]=numlist[m+1+y]
    i=0
    j=0
    k=l
    while i<n1 and j<n2 :
        if llist[i]<rlist[j]:
            numlist[k]=llist[i]
            i+=1
        else:
            numlist[k]=rlist[j]
            j+=1
        k+=1
    while i<n1:
        numlist[k]=llist[i]
        i+=1
        k+=1
    while j<n2:
        numlist[k]=rlist[j]
        j+=1
        k+=1


print("Merge Sort ")
n=int(input("Enter how many elements : "))
numbers_list=[]
for i in range(n):
    a=int(input("enter number : "))
    numbers_list.append(a)
print("Before sorting : ")
for a in numbers_list:
    print(a,end=" ")
merge_sort(numbers_list,0,len(numbers_list)-1)
print("\nAfter sorting : ")
for a in numbers_list:
    print(a,end=" ")