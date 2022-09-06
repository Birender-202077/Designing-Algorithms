# Implementation of quick sort in python

# creating a function to find the partition position
def partition(array, low, high):

  # choosing the rightmost element as pivot
  pivot = array[high]

  # making a pointer for greater element
  i = low - 1

  # comparing each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
  # if element smaller than pivot is found then swap it with the greater element pointed by i
      i = i + 1
  # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])
  # swaping the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# making a function which will perform quickSort 
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that element smaller than pivot are on the left 
    # and element greater than pivot are on the right
    a = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, a - 1)

    # recursive call on the right of pivot
    quickSort(array, a + 1, high)

#Test Case
ls=[]
ls = [int(x) for x in input("\nEnter the elements: ").split()]
print("\nUnsorted Array: ", ls)

size = len(ls)

quickSort(ls, 0, size - 1) #function call

print('\nSorted Array in Ascending Order: ',ls,'\n')
