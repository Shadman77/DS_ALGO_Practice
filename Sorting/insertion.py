#in each iter put the less valued element in place

def insertion_sort(arr):
    for i in range(1, len(arr)):
        insertion_target_index = i
        for j in range(i-1, -1, -1):
            if arr[j] > arr[insertion_target_index]:
                temp = arr[insertion_target_index]
                arr[insertion_target_index] = arr[j]
                arr[j] = temp
                insertion_target_index = j
    return arr


if __name__ == "__main__":
    arr = [10, 8, 5, 6, 4, 1, 2, 3, 7, 9]

    print(arr)
    print(insertion_sort(arr))