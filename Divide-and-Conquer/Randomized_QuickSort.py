"""this module is for Randomized Quicksort"""
import random

def randomized_quicksort(array, first_index, last_index): #average case O(n log n) and worst case o(n^(2))
    if(last_index>first_index):
        pivot = random_partition(array, first_index, last_index)
        randomized_quicksort(array, first_index, pivot - 1)
        randomized_quicksort(array, first_index + 1, pivot)



def random_partition(array, first_index, last_index):
    random_index = random.randint(first_index, last_index)
    array[last_index], array[random_index] = array[random_index], array[last_index]
    return partition(array, first_index, last_index)

def partition(array, first_index, last_index):
    pivot_value = array[last_index]
    small_element_tracker = first_index - 1
    for j in range(first_index, last_index):
        if array[j] <= pivot_value:
            small_element_tracker += 1
            array[small_element_tracker], array[j] = array[j], array[small_element_tracker]

    array[small_element_tracker + 1], array[last_index] = array[last_index], array[small_element_tracker + 1]
