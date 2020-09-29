#Search for a certain number in a list of numbers.
import math


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        mid = math.floor(left+(right-left)/2)
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6]
target = 6

output = binary_search(arr, target)

if output != -1:
    print(f"Element is at index {output}")
else:
    print("Element is not present in the array")
