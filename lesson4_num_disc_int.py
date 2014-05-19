#!/usr/bin/env python
# encoding: utf-8


# Lesson 4 - Sorting - Number of Disc Intersections
# https://codility.com/demo/take-sample-test/number_of_disc_intersections


def solution(A):
    '''
    Given an array A of N integers, we draw N discs in a 2D plane,
    such that the I-th disc is centered on (0,I) and has a radius of A[I].
    We say that the J-th disc and K-th disc intersect if:
    J != K and J-th and K-th discs have at least one common point.


    >>> solution([1, 5, 2, 3, 4, 0])
    11

    '''
    

    # declare variables
    intersections = 0
    max_intersections_value = 10000000


    #


    # return the result
    if intersections > max_intersections_value:
        return -1

    else:
        return intersections