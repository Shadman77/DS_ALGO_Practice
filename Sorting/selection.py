#in each iter get the lowest element and put it in its place

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp

    return arr


if __name__ == "__main__":
    arr = [10, 8, 5, 6, 4, 1, 2, 3, 7, 9]

    print(arr)
    print(selection_sort(arr))