def merge(left, right):
    result = []
    a = b = 0
    while a<len(left) and b<len(right):
        if left[a] < right[b]:
            result.append(left[a])
            a+=1
        else:
            result.append(right[b])
            b+=1
    result.extend(left[a:])
    result.extend(right[b:])
    return result

def sort(array):
    n = len(array)
    if n <= 1:
        return array

    mid = n // 2
    left_sorted = sort(array[0:mid])
    right_sorted = sort(array[mid:n])

    return merge(left_sorted, right_sorted)

if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 20, 15, 0, -3]
    print("Unsorted array: ", array)
    sorted_array = sort(array)
    print("Sorted array: ", sorted_array)
