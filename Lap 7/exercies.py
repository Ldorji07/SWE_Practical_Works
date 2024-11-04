
def in_place_quick_sort(arr, low=0, high=None):
    if high is None: high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        in_place_quick_sort(arr, low, pivot_index - 1)
        in_place_quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot, i = arr[high], low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1; arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped: break
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key, j = arr[i], i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def hybrid_merge_sort(arr, threshold=10):
    if len(arr) <= threshold:
        insertion_sort(arr); return arr
    mid = len(arr) // 2
    left, right = hybrid_merge_sort(arr[:mid], threshold), hybrid_merge_sort(arr[mid:], threshold)
    return merge(left, right)

def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

import matplotlib.pyplot as plt, matplotlib.animation as animation

def visualize_bubble_sort(arr):
    fig, ax = plt.subplots()
    def update(arr): ax.clear(); ax.bar(range(len(arr)), arr, color="skyblue")
    ani = animation.FuncAnimation(fig, update, frames=bubble_sort_gen(arr), repeat=False)
    plt.show()

def bubble_sort_gen(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr
