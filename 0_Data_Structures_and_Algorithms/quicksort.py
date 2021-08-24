"""
General Principle

Quicksort:

1. Choose pivot element (Usually last or random)
2. Stores elements less than pivot in left subarray
   Stores elements greater than pivot in right subarray
3. Call quicksort recursively on left subarray
   Call quicksort recursively on right subarray
"""


def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos -1)
        quicksort(arr, partition_pos + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1

        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


if __name__ == "__main__":
    arr = [22, 11, 88, 66, 55, 77, 33, 44]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)
