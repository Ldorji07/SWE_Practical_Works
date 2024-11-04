from heapq import merge


def quick_sort_in_place(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = partition(arr, low, high)
        quick_sort_in_place(arr, low, p - 1)
        quick_sort_in_place(arr, p + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high] 
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort_hybrid(arr):
    if len(arr) <= 10:  
        return insertion_sort(arr)
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_hybrid(arr[:mid])
    right = merge_sort_hybrid(arr[mid:])

    return merge(left, right)

import matplotlib.pyplot as plt
import numpy as np

def visualize_bubble_sort(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    bars = ax.bar(range(n), arr)
    ax.set_title("Bubble Sort Visualization")

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                for bar, value in zip(bars, arr):
                    bar.set_height(value)
                plt.pause(0.01)  
        if not swapped:
            break

    plt.show()

test_arr = [64, 34, 25, 12, 22, 11, 90]
visualize_bubble_sort(test_arr.copy())
