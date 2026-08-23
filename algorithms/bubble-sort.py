
def sort(array:list[int]) -> list[int]:
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break

    return array

if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 20, 15]
    print("Unsorted array: ", array)
    sorted_array = sort(array)
    print("Sorted array: ", sorted_array)
