#!/usr/bin/env python
# encoding: utf-8


# Lesson 2 - Counting Elements - Frog River One
# https://codility.com/demo/take-sample-test/frog_river_one


def solution(X, A):
    '''
    This function returns the earliest time when the frog can start jumping.
    Takes an int X, which is the destination and an array of leaves.
    The frog can jump only when all the leaves on it's path are down.
    The minute it happens so is returned.
    If such occurence doesn't happen, -1 is returned.

    (int, list of integers) -> int


    >>> solution(5, [1, 3, 1, 4, 2, 3, 5, 4])
    6
    
    '''
    
    sum_all = sum(xrange(1, X + 1))
    current_sum = 0
    
    leaves_set = set()
    
    for position, i in enumerate(A):
        if i not in leaves_set:
            current_sum += i
            leaves_set.add(i)

        if current_sum == sum_all:
            return position
    return -1
