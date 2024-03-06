def quicksort(nums,l,h):
    if l<h:
        partition_index=part(nums,l,h)
        quicksort(nums,l,partition_index-1)
        quicksort(nums,partition_index+1,h)

def part(nums,l,h):
    pivot=nums[l]
    i=l
    j=h
    while(i<j):
        while nums[i]<=pivot and i<=h-1 :
            i+=1
        while nums[j]>pivot and j>=l+1 :
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[l],nums[j]=nums[j],nums[l]
    return j

n=int(input("Enter how many elements : "))
numlist=[]
for i in range(n):
    a=int(input("Enter a number : "))
    numlist.append(a)
print("Before Sorting : ")
for a in numlist:
    print(a,end=" ")
quicksort(numlist,0,len(numlist)-1)
print("\nAfter Sorting : ")
for a in numlist:
    print(a,end=" ")