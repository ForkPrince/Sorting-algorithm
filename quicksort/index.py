from random import shuffle
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[pivot_index]:
            arr.insert(pivot_index, arr[i])
            arr.pop(i + 1)
            pivot_index += 1
    
    arr[0:pivot_index] = quicksort(arr[0:pivot_index])
    arr[pivot_index + 1:len(arr)] = quicksort(arr[pivot_index + 1:len(arr)])
    return arr
    

def main(s):
    unsorted_array = list(range(s))
    shuffle(unsorted_array)
    print("unsorted array: ", unsorted_array)
    start_time = time.time()
    sorted_array = quicksort(unsorted_array)
    end_time = time.time()

    elapsed_time = end_time - start_time
    print("sorted array ", sorted_array)
    print("elsapsed time: ", elapsed_time)



if __name__ == "__main__":
    size = input("Array size? ")
    main(int(size))