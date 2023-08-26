import random
import time
import threading

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

def sortChunk(arr, start, end):
    sorted_chunk = sorted(arr[start:end])
    return sorted_chunk

def bogoSortWithChunks(arr, chunk_size):
    startTime = time.time()
    iterations = 0

    while not isSorted(arr):
        threads = []
        sorted_chunks = []

        for i in range(0, len(arr), chunk_size):
            chunk_end = min(i + chunk_size, len(arr))
            thread = threading.Thread(target=lambda: sorted_chunks.append(sortChunk(arr, i, chunk_end)))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        print(sorted_chunks)
        arr = [element for chunk in sorted_chunks for element in chunk]
        shuffleArray(arr)

        iterations += 1

    endTime = time.time()
    elapsedTime = endTime - startTime

    return arr, iterations, elapsedTime

def main():
    unsorted_array = list(range(10, 0, -1))
    chunk_size = 5  # Adjust the chunk size as needed
    print("Unsorted array:", unsorted_array)

    sorted_array, iterations, elapsed_time = bogoSortWithChunks(unsorted_array.copy(), chunk_size)
    print("Sorted array:", sorted_array)
    print(f"Sorted in {iterations} iterations")
    print(f"Time elapsed: {elapsed_time:.6f} seconds")

if __name__ == "__main__":
    main()
