#!/usr/bin/env python3
# O(log n^2)

def get_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i, v in enumerate(arr):
        if v < smallest:
            smallest = v
            smallest_index = i
    
    return smallest_index


def selection_sort(arr):
    result = []

    for i in range(len(arr)):
        smallest = get_smallest(arr)
        result.append(arr.pop(smallest))
        
    
    return result


if __name__ == "__main__": 
   arr1 = [3,1,9,2,4]
   arr2 = [750, 100, 2000, 1, 50, 8000]

   print(selection_sort(arr1))
   print(selection_sort(arr2))
