#!/usr/bin/env python
# encoding: utf-8


# Lesson 3 - Prefix Sums - Passing Cars
# https://codility.com/demo/take-sample-test/passing_cars


def solution(A):
    '''
    An array with 0s and 1s is given, representing consecutive cars.
    0 - car travelling east, 1 - travelling west.
    Count the pairs of passing cars.

    >>> solution([0, 1, 0, 1, 1])
    5
    
    '''
    

    # declare variables
    pairs = 0
    current_sum = 0
    sums = [0] * len(A)
    max_passing_cars = 1000000000


    # calculate prefix sums
    for i, car in enumerate(A):
        current_sum += car
        sums[i] = current_sum


    # go through each car to calculate pairs variations
    # because we know how many 1s are in front of us
    for i, car in enumerate(A):
        if car == 0:
            pairs += sums[-1] - sums[i]


    # return the number of passing Cars
    if pairs > max_passing_cars:
        return -1

    else:
        return pairs