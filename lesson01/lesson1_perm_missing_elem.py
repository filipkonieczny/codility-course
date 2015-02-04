#!/usr/bin/env python
# encoding: utf-8


# Lesson 1 - Time Complexity - Perm Missing Element
# https://codility.com/demo/take-sample-test/perm_missing_elem


def solution(array):
    '''
    Find the missing number in an array of N different integers.
    The range of integers is [1, (N + 1)].
    Find the missing element.

    (list of integers) -> int

    >>> solution([2, 3, 1, 5])
    4

    '''

    array_length = len(array)
    array_sum = sum(array)
    expected_sum = (array_length + 1) * (array_length + 2) // 2
    return expected_sum - array_sum
