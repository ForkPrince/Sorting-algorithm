# import itertools
# import time

# def generate_and_test_sort(arr):
#     min_permutation = None
#     min_steps = float('inf')
    
#     for permutation in itertools.permutations(arr):
#         steps = 0
#         sorted_arr = list(permutation)
        
#         for i in range(len(sorted_arr)):
#             for j in range(i + 1, len(sorted_arr)):
#                 steps += 1
#                 if sorted_arr[i] > sorted_arr[j]:
#                     sorted_arr[i], sorted_arr[j] = sorted_arr[j], sorted_arr[i]
        
#         if steps < min_steps:
#             min_steps = steps
#             min_permutation = sorted_arr
    
#     return min_permutation

# unsorted_array = list(range(5, 0, -1))

# start_time = time.time()
# sorted_array = generate_and_test_sort(unsorted_array)
# end_time = time.time()

# iterations = len(list(itertools.permutations(unsorted_array)))
# elapsed_time = end_time - start_time

# print("Unsorted array:", unsorted_array)
# print("Sorted array:", sorted_array)
# print(f"Sorted in {iterations} iterations")
# print(f"Time elapsed: {elapsed_time:.6f} seconds")

# from itertools import permutations
# import time

# def sort(arr):
#     all_permutations = permutations(arr)
#     perms_list = list(all_permutations)
#     iterations = len(perms_list)

#     for idx, perm in enumerate(perms_list, start=1):
#         sorted_flag = True
#         for i in range(len(perm) - 1):
#             if perm[i] > perm[i + 1]:
#                 sorted_flag = False
#                 break
#         if sorted_flag:
#             return perm
#         print(f"Iteration {idx}/{iterations}: {perm}")

# unsorted_array = list(range(15, 0, -1))

# start_time = time.time()
# sorted_array = sort(unsorted_array)
# end_time = time.time()

# elapsed_time = end_time - start_time

# print("Unsorted array:", unsorted_array)
# print("Sorted array:", sorted_array)
# print(f"Sorted in {elapsed_time:.6f} seconds")

from itertools import permutations
from random import shuffle
import time

def sort(arr):
    all_permutations = permutations(arr)
    perms_list = list(all_permutations)
    iterations = len(perms_list)

    for idx, perm in enumerate(perms_list, start=1):
        sorted_flag = True
        for i in range(len(perm) - 1):
            if perm[i] > perm[i + 1]:
                sorted_flag = False
                break
        if sorted_flag:
            return perm
        print(f"Iteration {idx}/{iterations}: {perm}")

size = input("Array size? ")
unsorted_array = list(range(int(size)))
shuffle(unsorted_array)

start_time = time.time()
sorted_array = sort(unsorted_array)
end_time = time.time()

elapsed_time = end_time - start_time

print("Unsorted array:", unsorted_array)
print("Sorted array:", sorted_array)
print(f"Sorted in {elapsed_time:.6f} seconds")