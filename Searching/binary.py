from math import floor
def binary_search(arr, value, start = 0, end = None):
    if start == 0 and end == None:
        end = len(arr)-1
        arr.sort()

    if start == end:
        mid = start

        if arr[mid] == value:
            return True
        else:
            return False
    else:
        mid = floor(start + (end-start)/2)

        if arr[mid] == value:
            return True
        else:
            if value > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
            return binary_search(arr, value, start, end)



if __name__ == "__main__":
    arr = [1, 2, 10, 25, 4, 30, 3, 7]
    print(binary_search(arr, 7))
