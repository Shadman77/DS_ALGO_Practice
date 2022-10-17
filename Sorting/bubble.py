def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


if __name__ == "__main__":
    arr = [10, 8, 5, 6, 4, 1, 2, 3, 7, 9]

    print(arr)
    print(bubble_sort(arr))
