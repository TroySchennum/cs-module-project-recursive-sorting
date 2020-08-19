# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, low, high):
  
  middle = (low+high)/2
  if len(arr) == 0:
    return -1 # array empty
  elif low > high:
    return -1 # not found
  elif arr[middle] == target:
    return middle
  else:
    if target < arr[middle]:
      high = middle-1 # eliminate RHS
    else:      
      low = middle+1 # eliminate LHS
    return binary_search(arr, target, low, high)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
  
  low = 0
  high = len(arr) - 1
  middle = (low+high)//2
  # Base case
  ## if array is empty
  if len(arr) == 0:
    return -1 # array empty
  if arr[middle] == target:
    return middle
  else: 
    # Check if the target is above or below the middle
    if target > arr[middle]:
      one_half = arr[middle:high + 1]
      
    elif target < arr[middle]:
      one_half = arr[low:middle + 1]
    return agnostic_binary_search(one_half, target)

