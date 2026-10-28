"""This module is used to select the ith smallest element in an array,
since naive algorithms gives us running time of O(n lg n) we will use Divide and conquer to
reach O(n)"""

import random

def random_pivot(array, first_index, last_index):
    random_pivot = random.randint(first_index, last_index)
    array[random_pivot], array[last_index] = array[last_index], array[random_pivot]
    return partition(array, first_index, last_index)

def partition(array, first_index, last_index):
    pass