
'''
Problem 1
Write a python script in which you implement a function with an 3D 10x10x10 python array.
Fill that array with the first 1000 prime numbers.
Make the order random (non-consecutive). Return the filled array and print it in the console.
'''

import numpy as np
import random


def make_3d_arr(arr_len, shape, number):
    prime_numbers = []
    count = 0

    for num in range(2, number+1):
        prime = True
        for x in range(2, num):
            if num % x == 0:
                prime = False
                break

        if prime:
            prime_numbers.append(num)
        count = len(prime_numbers)

        if count == arr_len:
            break

    random.shuffle(prime_numbers)
    arr = np.array(prime_numbers).reshape(shape)
    print(arr)


if __name__ == '__main__':
    shape = (10, 10, 10)
    arr_len = 1000
    number = 10000
    make_3d_arr(arr_len, shape, number)

