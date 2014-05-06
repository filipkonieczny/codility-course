#!/usr/bin/env python
# encoding: utf-8


# Lesson 3 - Prefix Sums - Min Avg Two Slice
# https://codility.com/demo/take-sample-test/min_avg_two_slice


def solution(A):
    '''

    >>> solution([4, 2, 2, 5, 1, 5, 8])
    1

    '''
    

    # declare variables
    N = len(A)
    max_average = (A[0] + A[1]) / 2.0
    position = 0


    #
    i = 0

    while i + 2 < N:
        # calculate the average
        average = (A[i] + A[i + 1]) / 2.0

        # 2 element slice
        if average < max_average:
            position = i
            max_average = average


        # 3 element slice
        if (A[i] + A[i + 1] + A[i + 2]) / 3.0 < max_average:
            position = i
            max_average = (A[i] + A[i + 1] + A[i + 2]) / 3.0


        i += 1


    # last 2 element slice
    if (A[-1] + A[-2]) / 2.0 < max_average:
        position = N - 2


    # return the smallest slice's starting position
    return position

result = solution([0, 0, 0, 0])

print result