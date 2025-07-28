from math import floor

def merge_sort(arr):
    if len(arr) > 1:
        # dividing the array into two parts until not possible anymore
        arr1 = merge_sort(arr[:floor(len(arr)/2)])
        arr2 = merge_sort(arr[floor(len(arr)/2):])
        arr = []

        # arranging the elements of both the sorted arrays to form a sorted combined array
        while(len(arr1) > 0 or len(arr2) > 0):
            if len(arr2) == 0:
                arr.append(arr1.pop(0))
            elif len(arr1) == 0:
                arr.append(arr2.pop(0))
            else:
                a = arr1[0]
                b = arr2[0]
                if a < b:
                    arr.append(a)
                    arr1.pop(0)
                else:
                    arr.append(b)
                    arr2.pop(0)
        return arr
    else:
        return arr


if __name__ == "__main__":
    arr = [10, 8, 5, 6, 4, 1, 2, 3, 7, 9]
    print(arr)
    print(merge_sort(arr))

    arr = [8, 5, 6, 4, 1, 2, 3, 7, 9]
    print(arr)
    print(merge_sort(arr))