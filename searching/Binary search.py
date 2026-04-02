def binary_search(arr,target):
    size = len(arr)
    start =0
    end = size -1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


sorted_list = [1,2,3,4,5,6,7,8,9,10]
target = 5
print(binary_search(sorted_list,target))