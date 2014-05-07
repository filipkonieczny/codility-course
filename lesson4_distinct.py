#!/usr/bin/env python
# encoding: utf-8


# Lesson 4 - Sorting - Distinct
# https://codility.com/demo/take-sample-test/distinct


def solution(A):
    '''
    An array A is given. Return the number of distinct numbers.

    >>> solution([2, 1, 1, 2, 3, 1])
    3

    '''
    

    # declare variables
    N = len(A)
    A = sorted(A)
    result = 1


    # corner case - empty list
    if N == 0:
    	return 0


    # iterate through sorted A list and notice any different numbers
    for i in xrange(N - 1):
    	if A[i] != A[i + 1]:
    		result += 1


    # return the result
    return result