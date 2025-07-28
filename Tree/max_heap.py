# * Reference: https://www.youtube.com/watch?v=HqPJF2L5h9U

"""
left_child(i)=2i+1
right_child(i)=2i+2
parent(i)=floor((i-1)/2) = if i != 0

Where i is the index of the current node
"""

import math


arr = []

def insert(val):
    arr.append(val)
    i = len(arr) - 1
    while i > 0:
        parent = math.floor((i-1)/2)
        if arr[parent] < arr[i]:
            arr[parent], arr[i] = arr[i], arr[parent] # * Actually I didn't know this syntax for swapping
            i = parent
        else:
            break


def delete():
    if not arr:
        return None
    
    if len(arr) == 1:
        return arr.pop()
    
    max_val = arr[0]
    arr[0] = arr.pop()

    
    

    i = 0
    while 2*i+1 < len(arr):
        pi1 = 2*i+1
        pi2 = 2*i+2
        current = i

        if pi2 >= len(arr):
            i = pi1
        else:
            i = pi1 if arr[pi1] > arr[pi2] else pi2

        if arr[current] > arr[i]:
            break

        arr[current], arr[i] = arr[i], arr[current]

    return max_val

if __name__ == "__main__":
    while True:
        print("1 = Insert, 2 = Delete, 3 = Print")
        choice = input()
        if choice == "1":
            val = int(input("Enter value to insert: "))
            insert(val)
        elif choice == "2":
            print("Max val =", delete())
        elif choice == "3":
            print("Max Heap:", arr)
        else:
            print("Invalid choice")
