import random
import time

def deterministic_partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def deterministic_quick_sort(arr, low, high):
    if low < high:
        pivot = deterministic_partition(arr, low, high)
        deterministic_quick_sort(arr, low, pivot-1)
        deterministic_quick_sort(arr, pivot+1, high)

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot-1)
        randomized_quick_sort(arr, pivot+1, high)

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = [random.randint(1, 1000) for _ in range(n)]
    iterations = int(input("Enter the number of iterations for analysis: "))

    print("Analysis of Deterministic Quick Sort:")
    deterministic_time = 0.0

    for _ in range(iterations):
        arr_copy = arr.copy()
        start_time = time.time()
        deterministic_quick_sort(arr_copy, 0, n - 1)
        end_time = time.time()
        deterministic_time += end_time - start_time

    print("Average time taken for", iterations, "iterations:", deterministic_time / iterations, "seconds")

    print("\nAnalysis of Randomized Quick Sort:")
    randomized_time = 0.0

    for _ in range(iterations):
        arr_copy = arr.copy()
        start_time = time.time()
        randomized_quick_sort(arr_copy, 0, n - 1)
        end_time = time.time()
        randomized_time += end_time - start_time

    print("Average time taken for", iterations, "iterations:", randomized_time / iterations, "seconds")

if __name__ == "__main__":
    main()
