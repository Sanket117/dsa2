def linear_search(arr,target):
    size = len(arr)
    for i in range(0,size):
        if arr[i]==target:
            return i 
        else:
            return -1



my_list = [10,24,35,70,11]
target =70

result = linear_search(my_list,target)
print(result)