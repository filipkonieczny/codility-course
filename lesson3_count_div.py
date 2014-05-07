#!/usr/bin/env python
# encoding: utf-8


# Lesson 3 - Prefix Sums - Count Div
# https://codility.com/demo/take-sample-test/count_div


def solution(A, B, K):
    '''

    >>> solution(6, 11, 2)
    3

    '''
    

    # if A is dividable by K
    if A % K == 0:
        return (B - A) / K + 1

    else:
        return (B - (A - A % K)) / K