#!/usr/bin/env python
# encoding: utf-8


# Lesson 3 - Prefix Sums - Max Product of Three
# https://codility.com/demo/take-sample-test/max_product_of_three


def solution(A):
    '''
    Array A is given and you need to return the biggest product of any triplet.
    Triplet is a combination of 3 distinctive values.
    Each value is a position of a number in the array.

    Biggest value can be achieved by multiplying 2 lowest negative numbers
    by 1 biggest positive number, or 3 biggest positive numbers.

    >>> solution([-3, 1, 2, -2, 5, 6])
    60

    '''
    

    # declare variables
    A = sorted(A)
    product1 = 0
    product2 = 0


    # 2 lowest and the biggest
    product1 = A[0] * A[1] * A[-1]


    # 3 biggest
    product2 = A[-1] * A[-2] * A[-3]


    # return the result
    if product2 > product1:
        return product2

    return product1