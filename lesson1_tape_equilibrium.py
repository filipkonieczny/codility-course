#!/usr/bin/env python
# encoding: utf-8


# Lesson 1 - Time Complexity - TapeEquilibrium
# https://codility.com/demo/take-sample-test/tape_equilibrium


def solution(A):
    '''
    This function splits an array of integers into 2 tapes.
    Calculates the absolute difference between the sum of those 2 tapes.
    Returns the smallest difference.
    
    
    (list of integers) -> int
    
    
    >>> solution([3, 1, 2, 4, 3])
    1
    
    Because abs((3 + 1 + 2) - (4 + 3)) = 1
    
    '''
    
    
    # declare variables
    difference = 0
    result = 0
    sum_after_p = 0
    sum_before_p = A[0]
    
    
    # sum all elements
    for i in range(1, len(A)):
        sum_after_p += A[i]


    # calculate the value of result for the 1st element
    result = abs(sum_before_p - sum_after_p)
    
    
    # calculate the difference
    for i in range(1, len(A)):
        difference = abs(sum_before_p - sum_after_p)
        
        if difference < result:
            result = difference
        
        sum_before_p += A[i]
        sum_after_p -= A[i]
    
    
    # return the result
    return result