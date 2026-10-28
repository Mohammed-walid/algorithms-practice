"""this module is for Randomized Quicksort"""
import random

def randomized_quicksort(array, first_index, last_index):
    if(last_index>first_index):
        pivot = random_partition(array, first_index, last_index)
        randomized_quicksort(array, first_index, pivot - 1)
        randomized_quicksort(array, first_index + 1, pivot)



def random_partition(array, first_index, last_index):
    random_index = random.randint(first_index, last_index)
    array[last_index], array[random_index] = array[random_index], array[last_index]
    return partition(array, first_index, last_index)

def partition(array, first_index, last_index):
    pass