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
    n = len(A)
    numbers = [0] * n
    
    
    # iterate through every element of the list to count each occurence
    for i in A:
        # check if an element is not bigger than our array
        if i <= n:
            numbers[i - 1] += 1

        # if an element is out of range instantly stop
        else:
            return 0
    
    
    # iterate through the list of counted occurences
    for i in numbers:
        # if any of the occurences happened more than once(> 1), or never(= 0)
        if i != 1:
            return 0


    # if everything's ok it means that the list is permuted
    return 1