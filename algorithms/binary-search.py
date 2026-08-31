def search(array:list[int], k:int) -> int:
    left = 0
    right = len(array)
    while left < right:
        mid = (left+right)//2
        mid_element = array[mid]
        if mid_element == k:
            return mid
        if left == mid:
            return -1
        if mid_element < k:
            left = mid
        else:
            right = mid

if __name__ == "__main__":
    array = [1,3,5,8,9,10,14,35,67,89,94,100]
    print("Given array: ", array)
    nums_to_search = [5,9,66,8,100,15,102]
    for k in nums_to_search:
        index = search(array,k)
        if index >= 0:
            print(k, "was found at index", index)
        else:
            print(k, "was not found!")


