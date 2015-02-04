#!/usr/bin/env python
# encoding: utf-8


# Lesson 1 - Time Complexity - Tape Equilibrium
# https://codility.com/demo/take-sample-test/tape_equilibrium


def solution(array):
    '''
    This function splits an array of integers into 2 tapes.
    Calculates the absolute difference between the sum of those 2 tapes.
    Returns the smallest difference.


    (list of integers) -> int


    >>> solution([3, 1, 2, 4, 3])
    1

    Because abs((3 + 1 + 2) - (4 + 3)) = 1

    '''

    prev_sum = array[0]
    next_sum = sum(array) - array[0]
    result = abs(prev_sum - next_sum)

    for i in range(1, len(array)):
        difference = abs(prev_sum - next_sum)

        if difference < result:
            result = difference

        prev_sum += array[i]
        next_sum -= array[i]

    return result
