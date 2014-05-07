#!/usr/bin/env python
# encoding: utf-8


# Lesson 4 - Sorting - Triangle
# https://codility.com/demo/take-sample-test/triangle


def solution(A):
    '''
    Find if there's a triplet(combination of 3 values) that's triangular.

    >>> solution([10, 2, 5, 1, 8, 2])
    1

    >>> [10, 50, 5, 1]
    0

    '''
    

    # declare variables
    A = sorted(A)
    n = len(A)


    # search for triplets
    for i in xrange(1, n - 1):
        if A[-i] + A[-i - 1] > A[-i - 2] and \
        A[-i] + A[-i - 2] > A[-i - 1] and \
        A[-i - 2] + A[-i - 1] > A[-i]:
            return 1


    # return the result
    return 0