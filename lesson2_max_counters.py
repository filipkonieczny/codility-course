#!/usr/bin/env python
# encoding: utf-8


# Lesson 2 - Counting Elements - Max Counters
# https://codility.com/demo/take-sample-test/max_counters


def solution(N, A):
    '''
    This function receives an int and an array of integers.
    Performs counters check on that list and returns them.
    Two operations can be performed.
    Increase(X) - counter X is increased by 1.
    Max_counter - all counters are set to the maximum value of any counter.

    (int, list of integers) -> list of integers


    >>> solution(5, [3, 4, 4, 6, 1, 4, 4]) -> list of integers
    [3, 2, 2, 4, 2]
    
    '''
    

    # declare variables
    counters = [0] * N
    max_counter = 0
    increased_N = N + 1


    # calculate the value of counters
    for i in A:
        # check if to perform increase all counters
        if i == increased_N:
            counters = [max_counter] * N

        # if not, then increase counter by 1
        else:
            counters[i - 1] += 1
            foo = counters[i - 1]

            if foo > max_counter:
                max_counter = foo


    # return the values of counters
    return counters