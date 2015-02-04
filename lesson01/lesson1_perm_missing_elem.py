#!/usr/bin/env python
# encoding: utf-8


# Lesson 1 - Time Complexity - Perm Missing Element
# https://codility.com/demo/take-sample-test/perm_missing_elem


def solution(A):
    '''
    Find the missing number in an array of N different integers.
    The range of integers is [1, (N + 1)].
    Find the missing element.
    
    
    (list of integers) -> int
    
    
    >>> solution([2, 3, 1, 5])
    4
    
    '''
    
    
    # declare variables
    sum_elements = 0
    sum_series = 0
    n = len(A) + 1
    
    
    # sum all of the elements of the list
    for i in A:
        sum_elements += i
    
    # sum the series
    sum_series = n * (n + 1) / 2
    
    
    # return the missing number
    return sum_series - sum_elements