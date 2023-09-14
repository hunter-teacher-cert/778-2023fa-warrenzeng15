# Binary Search
# Warren Zeng
# CSCI 77800 Fall 2023
# collaborators: 
# consulted: 


def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = int((low + high)/2) 

        if array[mid] == target:
            return mid  # mid is the target so we return its index
        elif array[mid] < target:
            low = mid + 1  # target value is in the right half
        else:
            high = mid - 1  # target value  is in the left half

    return -1  # not found

#example
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
target = 5

print("Target:", target,  "found at index", binary_search(array, target))

