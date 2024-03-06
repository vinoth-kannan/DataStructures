def heapsort(nums):
    n=len(nums)
    for i in range(n//2,-1,-1):
        maxheap(nums,n,i)
    for i in range(n-1,0,-1):
        nums[i],nums[0]=nums[0],nums[i]
        maxheap(nums,i,0)

def maxheap(arr,n,parent_index):
    largest=parent_index
    left=2*parent_index+1
    right=2*parent_index+2
    if left < len(arr) and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest!=parent_index:
        arr[largest],arr[parent_index]=arr[parent_index],arr[largest]
        maxheap(arr,n,largest)


arr=[10,45,23,1,67,2]
heapsort(arr)
print(arr)