'''
Binary Search Problem

Returns index of x in arr if present, elsewhere it will return -1.

'''
#making a function named binary_search
def binary_search(list, key):
    low = 0
    high = len(list) - 1
    mid = 0

    # Checking base case
    while low <= high:
        mid = (high + low) // 2
    # If element is smaller than mid, then it can only be present in left subarray
        if list[mid] < key:
          low = mid + 1
    # If the element is greater than mid, the element can only be present in right subarray
        elif list[mid] > key:
           high = mid + 1
    # Else it will be present in the mid
        else:
           return mid
           
    return -1 #If the element is not present in the list.


# test case of a list
list = [11,2,31,4,32,4,61,32]
key = 61

# Function Call
result = binary_search(list, key)
if result != -1:
    print("Element is present at index : ", str(result))
else:
    print("Element is not present in the list.")