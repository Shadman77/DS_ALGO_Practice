def counting_sort(arr):
    store = [0] * 100 # considering range as 100
    for elem in (arr):
        store[elem] += 1

    arr = []
    for i in range(len(store)):
        for j in range(store[i]):
            arr.append(i)

    return arr


if __name__ == "__main__":
    arr = [10, 8, 5, 6, 4, 1, 2, 3, 7, 9]

    print(arr)
    print(counting_sort(arr))
