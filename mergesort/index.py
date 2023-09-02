from random import shuffle
from math import ceil
import time

def mergesort(arr):
    if len(arr) <= 2:
        if len(arr) <= 1:
            return arr
        if arr[0] > arr[1]:
            arr.append(arr[0])
            arr.pop(0)
        return arr
    
    arr[0:ceil(len(arr)/2)], arr[ceil(len(arr)/2):len(arr)] = mergesort(arr[0:ceil(len(arr)/2)]), mergesort(arr[ceil(len(arr)/2):len(arr)])
    arr2 = []

    i, i2 = 0, ceil(len(arr)/2)

    while i < ceil(len(arr)/2) and i2 < len(arr):
        if arr[i] <= arr[i2]:
            arr2.append(arr[i])
            i += 1
        else:
            arr2.append(arr[i2])
            i2 += 1
    while i < ceil(len(arr)/2):
        arr2.append(arr[i])
        i += 1
    while i2 < len(arr):
        arr2.append(arr[i2])
        i2 += 1
    
    arr = arr2
    return arr
    

def main(s):
    array = list(range(s))
    shuffle(array)
    print("unsorted array: ", array)
    start_time = time.time()
    array = mergesort(array)
    end_time = time.time()

    elapsed_time = end_time - start_time
    print("sorted array ", array)
    print("elsapsed time: ", elapsed_time)



if __name__ == "__main__":
    size = input("Array size? ")
    main(int(size))