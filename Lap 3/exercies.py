def linear_search_all(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices if indices else -1

def binary_search_insertion_point(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left  

def linear_search_count(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

def binary_search_count(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

import math

def jump_search(arr, target):
    length = len(arr)
    step = int(math.sqrt(length))
    prev = 0

    while arr[min(step, length) - 1] < target:
        prev = step
        step += int(math.sqrt(length))
        if prev >= length:
            return -1

    for i in range(prev, min(step, length)):
        if arr[i] == target:
            return i
    return -1

def test_jump_search():
    arr = list(range(0, 10000, 2))  
    target = 8888
    result = jump_search(arr, target)
    print(f"Jump Search: Found at index {result}")

test_jump_search()
