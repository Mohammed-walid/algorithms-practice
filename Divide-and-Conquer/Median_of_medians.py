"""To eliminate the terrible O(n^(2)) worst case of select ith smallest element
median of median method chooses the perfect pivot, so the complexity will be O(n)
if the amount of work at each recursive level shrinks fast enough"""

def find_median(array):
    array.sort()
    return array[len(array) // 2]

def median_of_medians(array, target_rank):
    sublists = [array[j:j + 5] for j in range(0, len(array), 5)]
    medians = [find_median(sublist) for sublist in sublists]

    if len(medians) <= 5:
        pivot = find_median(medians)
    else:
        pivot = median_of_medians(medians, len(medians) // 2)

    low = [j for j in array if j < pivot]
    high = [j for j in array if j > pivot]

    smaller_elements_count = len(low)

    if target_rank < smaller_elements_count:
        return median_of_medians(low, target_rank)
    elif target_rank > smaller_elements_count:
        return median_of_medians(high, target_rank - smaller_elements_count - 1)
    else:
        return pivot
