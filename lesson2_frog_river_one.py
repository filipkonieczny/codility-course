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
    

    # declare variables
    K = 0
    leaves = [0] * X
    number_of_leaves = 0


    # go through the list
    for i, item in enumerate(A):
        if item <= X:
            if leaves[item - 1] == 0:
                number_of_leaves += 1

                if number_of_leaves == X:
                    K = i
                    break

            leaves[item - 1] += 1


    # return the result
    # if not enough leaves found
    if number_of_leaves != X:
        return -1

    # if enough leaves found
    else:
        return K