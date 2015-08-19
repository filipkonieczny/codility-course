#!/usr/bin/env python
# encoding: utf-8


# Lesson 2 - Counting Elements - Perm Check
# https://codility.com/demo/take-sample-test/perm_check


def solution(A):
    '''
    This function takes an array of integers and checks if it's permuted.
    Permutation is when every element of the list occurs only once.
    Values of the elements in range from 1 to n, where n is the array's length.


    (list of integers) -> int


    >>> solution([4, 1, 3, 2])
    1

    >>> solution([4, 1, 3])
    0
    
    '''
    

    # declare variables
    there_should_be = [i for i in xrange(1, len(A) + 1)]
    there_is = sorted(A)
    
    if there_should_be == there_is:
        return 1
    return 0
