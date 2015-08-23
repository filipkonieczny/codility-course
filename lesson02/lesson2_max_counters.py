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
    
    counters = [0] * N
    increased_N = N + 1
    max_value = 0
    current_counter = 0

    for i in A:
        if i < increased_N:
            if counters[i - 1] < current_counter:
                counters[i - 1] = current_counter

            counters[i - 1] += 1

            if counters[i - 1] > max_value:
                max_value = counters[i - 1]
        else:
            current_counter = max_value

    for i in xrange(N):
        if counters[i] < current_counter:
            counters[i] = current_counter

    return counters
