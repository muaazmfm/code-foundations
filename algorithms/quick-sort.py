def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i+1, high)
    return i+1

def sort(array, low=0, high=None):
    if high == None:
        high = len(array)-1

    if low<high:
        pivot_idx = partition(array, low, high)
        sort(array, low, pivot_idx-1)
        sort(array, pivot_idx, high)

if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, -5, 4, 3, 2, 1, 10, 20, -15, 0, -3]
    print("Unsorted array: ", array)
    sort(array)
    print("Sorted array: ", array)
