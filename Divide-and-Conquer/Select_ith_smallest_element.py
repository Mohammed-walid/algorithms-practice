"""This module is used to select the ith smallest element in an array,
since naive algorithms gives us running time of O(n lg n) we will use Divide and conquer to
reach O(n), but worst case is O(n^(2)) so we want to eliminte it we will be implementing
Median of medians method"""

import random

def random_pivot(array, first_index, last_index):
    random_index = random.randint(first_index, last_index)
    array[random_index], array[last_index] = array[last_index], array[random_index]
    return partition(array, first_index, last_index)

def partition(array, first_index, last_index):
    pivot_value  = array[last_index]
    small_element_tracker = first_index - 1
    for j  in range(first_index, last_index):
        if pivot_value >= array[j]:
            small_element_tracker += 1
            array[small_element_tracker], array[j] = array[j], array[small_element_tracker]

    array[small_element_tracker + 1], array[last_index] = array[last_index], array[small_element_tracker + 1]
    return small_element_tracker + 1

def rand_select(array, first_index, last_index, ith_smallest_number):
    if first_index == last_index:
        return array[first_index]
    final_index = random_pivot(array, first_index, last_index)
    pivot_rank = final_index - first_index + 1
    if pivot_rank == ith_smallest_number:
        return array[final_index]
    elif ith_smallest_number < pivot_rank:
        return rand_select(array, first_index, final_index-1, ith_smallest_number)
    else:
        return rand_select(array, final_index + 1, last_index, ith_smallest_number - pivot_rank)
