# -*- coding: utf-8 -*-

import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

data_size = [10, 100, 1000]
for size in data_size:
    data = random.sample(range(1, size * 10), size)

    start_time = time.time()
    bubble_sort(data.copy())
    print(f"Bubble Sort ({size}): {time.time() - start_time:.6f} seconds")

    start_time = time.time()
    merge_sort(data.copy())
    print(f"Merge Sort ({size}): {time.time() - start_time:.6f} seconds")
