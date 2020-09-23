#!/usr/bin/env python3

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
    return None


if __name__ == "__main__": 
   arr1 = [1, 2, 3, 4, 5, 6, 7]
   arr2 = [10, 100, 2000, 4000, 7500, 12000]

   print(binary_search(arr1, 2))
   print(binary_search(arr1, 6))
   print(binary_search(arr1, 4))
   print(binary_search(arr1, 10))
   print(binary_search(arr1, -1))

   print(binary_search(arr2, 4000))
   print(binary_search(arr2, 12000))


