import random

def replace(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def random_quick(arr, start, end, ret = True):
    pivot = random.randint(start, end)
    replace(start, pivot, arr)
    pivot = start #since pivot is not start
    for i in range(start+1, end+1):
        if arr[i] <= arr[start]:
            pivot += 1
            replace(pivot, i, arr)
    replace(pivot, start, arr)
    if pivot > start:
        random_quick(arr, start, pivot-1, ret = False)
    if pivot < end:
        random_quick(arr, pivot, end, ret = False)
    if ret:
        return arr


if __name__ == "__main__":
    # arr = [100, 80, 25, 46, 554, 351, 52, 3, 37, 439, 80, 25, 46, 554, 351, 52]
    arr = [44,76,5,87,8,5,88,66,54,23,1,787,-1,0]
    print(arr)
    print(random_quick(arr, 0, len(arr) - 1))