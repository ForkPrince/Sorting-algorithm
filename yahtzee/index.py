import random
import time

def getRandom():
    return random.random()

def isSorted(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True

def shuffleArray(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = int(getRandom() * (i + 1))
        arr[i], arr[j] = arr[j], arr[i]
        print(arr)

def modifiedBogoSort(arr, chunk_size):
    startTime = time.time()
    iterations = 0

    while not isSorted(arr):
        correct_pieces = []
        incorrect_pieces = []

        for i in range(0, len(arr), chunk_size):
            chunk = arr[i:i + chunk_size]
            if isSorted(chunk):
                correct_pieces.append(chunk)
            else:
                incorrect_pieces.append(chunk)

        if incorrect_pieces:
            for piece in incorrect_pieces:
                shuffleArray(piece)
        else:
            for piece in correct_pieces:
                shuffleArray(piece)

        arr = [element for chunk in (correct_pieces + incorrect_pieces) for element in chunk]

        iterations += 1

    endTime = time.time()
    elapsedTime = endTime - startTime

    return arr, iterations, elapsedTime

def main(s):
    unsorted_array = list(range(s))
    random.shuffle(unsorted_array)

    length = len(unsorted_array)
    chunk_size = length // 5

    if length <= 5:
        chunk_size = 2

    # chunk_size = 3 # Adjust the chunk size as needed

    print("Unsorted array:", unsorted_array)

    sorted_array, iterations, elapsed_time = modifiedBogoSort(unsorted_array.copy(), chunk_size)
    print("Sorted array:", sorted_array)
    print(f"Sorted in {iterations} iterations")
    print(f"Time elapsed: {elapsed_time:.6f} seconds")

if __name__ == "__main__":
    size = input("Array size? ")
    main(int(size))
