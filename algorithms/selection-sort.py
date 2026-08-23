
def sort(array:list[int]) -> list[int]:
    n = len(array)
    for i in range(n):
        next_min_idx = i
        for j in range(i+1, n):
            if array[j] < array[next_min_idx]:
                next_min_idx = j
        array[i], array[next_min_idx] = array[next_min_idx], array[i]

    return array

if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 20, 15, 0, -3]
    print("Unsorted array: ", array)
    sorted_array = sort(array)
    print("Sorted array: ", sorted_array)
