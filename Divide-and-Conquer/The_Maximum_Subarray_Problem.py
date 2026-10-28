"""This module contains 2 functions a helper function and the maximum subarray function"""

def find_max_crossing_subarray(arr, low, mid, high): #this function takes O(n)
    left_sum = float('-inf') #so our first sum becomes the max left sum
    right_sum = float('-inf')
    summion = 0
                 #(start point, end point, step by)
    for i in range(mid, low-1, -1):
        summion = summion + arr[i]
        if summion > left_sum: #high score tracker
            left_sum = summion
            max_left_index = i #the exact starting index of the highest sum

    summion = 0
    for j in range(mid+1, high+1):
        summion = summion + arr[j]
        if summion > right_sum:
            right_sum = summion
            max_right_index = j

    return max_left_index, max_right_index, left_sum + right_sum


def find_maximum_subarray(arr, low, high): # Algorithm is O(n log n)
    if high == low: #if array contains 1 element only
        return low, high, arr[low]

    else:
        mid = (low+high)//2
        left_low, left_high, left_sum = find_maximum_subarray(arr, low, mid)

        right_low, right_high, right_sum = find_maximum_subarray(arr, mid+1, high)

        cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum










if __name__ == "__main__":
    array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

    start_index = 0
    end_index = len(array) - 1

    best_low, best_high, max_sum = find_maximum_subarray(array, start_index, end_index)

    print(f"Array: {array}")
    print(f"Maximum Contiguous Sum: {max_sum}")
    print(f"Found between index {best_low} and {best_high}")
    print(f"Subarray elements: {array[best_low:best_high + 1]}")
