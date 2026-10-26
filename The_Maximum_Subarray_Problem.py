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
    for j in range(mid+1, high):
        summion = summion + arr[j]
        if summion > right_sum:
            right_sum = summion
            max_right_index = j

    return (max_left_index, max_right_index, left_sum + right_sum)


def find_maximum_subarray(arr, low, high):
    if high == low: #if array contains 1 element only
        return (low, high, arr[low])

    else:
        mid = (low+high)//2
        left_low, left_high, left_sum = find_maximum_subarray(arr, low, mid)

        right_low, right_high, right_sum = find_maximum_subarray(arr, mid+1, high)

        cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)












if __name__ == "__main__":
    pass