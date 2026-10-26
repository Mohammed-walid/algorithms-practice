"""This module is used to implement karatsuba's Algorithm"""

def karatsuba(x, y): #this algorithm is O(n^(1.59))
    if x < 10 and y < 10:
        return x*y

    x_length = len(str(x)) #converted x to string since numbers dont have a length
    y_length = len(str(y))

    if(x_length > y_length):
        n = x_length
    else:
        n = y_length

    half_n = n//2
    power = 10 ** half_n

    x_left = x // power
    x_right = x % power
    y_left = y // power
    y_right = y % power

    #karatsuba's trick,  conquer
    step1 = karatsuba(x_right, y_right)
    step2 = karatsuba(x_left, y_left)
    step3 = karatsuba((x_left + x_right), (y_left + y_right))

    #combine
    middle_term = step3-step2-step1

    #final formula
    result = (step2 * (10 ** (2 * half_n))) + (middle_term * (10 ** half_n)) + step1

    return result



if __name__ == "__main__":
    print(karatsuba(1234,5678))