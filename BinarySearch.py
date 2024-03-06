def binary_search(numbers,l,h,tar):
    if l<=h:
        mid = (l + h) // 2
        if numbers[mid]==tar:
            return mid
        elif numbers[mid]>tar:
            return binary_search(numbers,l,mid-1,tar)
        else:
            return binary_search(numbers,mid+1,h,tar)
    else:
        return -1
n=int(input("Enter number of elements: "))
numbers_list=[]
for i in range(n):
    a=int(input("Enter number : "))
    numbers_list.append(a)
numbers_list.sort()
target=int(input("Enter search element : "))
ind = binary_search(numbers_list,0,len(numbers_list)-1,target)
if ind==(-1) :
    print("Element not found")
else:
    print(f"{target} found at position {ind+1}")