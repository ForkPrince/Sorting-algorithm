from random import shuffle
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    arr1, arr2 = [], []
    pivot = arr[0]
    for i in arr[1:len(arr)]:
        if i < pivot:
            arr1.append(i)
        else:
            arr2.append(i)
    arr1 = quicksort(arr1)
    arr2 = quicksort(arr2)

    arr = arr1 + [pivot] + arr2
    return arr
    

def main(s):
    unsorted_array = list(range(s))
    shuffle(unsorted_array)
    start_time = time.time()
    sorted_array = quicksort(unsorted_array)
    end_time = time.time()

    elapsed_time = end_time - start_time
    print("unsorted array: ", unsorted_array)
    print("sorted array ", sorted_array)
    print("elsapsed time: ", elapsed_time)



if __name__ == "__main__":
    size = input("Array size? ")
    main(int(size))