import timeit
import random
import matplotlib.pyplot as plt
import numpy as np


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]


def measure_time(sort_func, arr):
    return timeit.timeit(lambda: sort_func(arr.copy()), number=1)


def compare_algorithms():
    sizes = [100, 1000, 5000, 10000]
    merge_times = []
    insertion_times = []
    timsort_times = []

    for size in sizes:
        arr = generate_random_array(size)

        # Measure merge sort
        merge_time = measure_time(merge_sort, arr)
        merge_times.append(merge_time)

        # Measure insertion sort
        insertion_time = measure_time(insertion_sort, arr)
        insertion_times.append(insertion_time)

        # Measure Timsort (Python's built-in sort)
        timsort_time = measure_time(lambda x: x.sort(), arr)
        timsort_times.append(timsort_time)

        print(f"\nArray size: {size}")
        print(f"Merge Sort time: {merge_time:.6f} seconds")
        print(f"Insertion Sort time: {insertion_time:.6f} seconds")
        print(f"Timsort time: {timsort_time:.6f} seconds")

    # Plotting results
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, merge_times, 'b-', label='Merge Sort')
    plt.plot(sizes, insertion_times, 'r-', label='Insertion Sort')
    plt.plot(sizes, timsort_times, 'g-', label='Timsort')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Sorting Algorithms')
    plt.legend()
    plt.grid(True)
    plt.savefig('sorting_comparison.png')
    plt.close()


if __name__ == "__main__":
    print("Comparing sorting algorithms...")
    compare_algorithms()
    print("\nAnalysis complete! Check sorting_comparison.png for the visualization.")
