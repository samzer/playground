#!/usr/bin/env python3
# O(nlog n)

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        l, r , p = partition(arr, len(arr)//2)
        return quick_sort(l) + [p] + quick_sort(r)


def partition(arr, pivot):
    left = []
    right = []
    p = arr[pivot]

    for i, v in enumerate(arr):
        if i == pivot:
            continue
        
        if v <= pivot:
            left.append(v)
        
        if v > pivot:
            right.append(v)
        
    return left, right, p


if __name__ == "__main__": 
   arr1 = [3,1,9,2,4]
   arr2 = [750, 100, 2000, 1, 50, 8000]
   arr3 = [3,4,3,4,3,4]

   print(quick_sort(arr1))
   print(quick_sort(arr2))
   print(quick_sort(arr3))
