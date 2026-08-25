def swap(array, a, b):
    array[a], array[b] = array[b], array[a]

def sort(array:list[int]) -> list[int]:
    n = len(array)
    for i in range(n):
        j=i
        while j>0 and array[j]<array[j-1]:
            swap(array, j, j-1)
            j-=1

    return array

if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 20, 15, 0, -3]
    print("Unsorted array: ", array)
    sorted_array = sort(array)
    print("Sorted array: ", sorted_array)
