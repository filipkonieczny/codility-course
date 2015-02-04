#!/usr/bin/env python
# encoding: utf-8


# Lesson 1 - Time Complexity - FrogJmp
# https://codility.com/demo/take-sample-test/frog_jmp


def solution(start_pos, finish_pos, jumping_distance):
    '''
    Takes start and finish positions, along with a jumping distance.
    Calculates how many jumps are needed to get from start to finish.

    (int, int, int) -> int


    >>> solution(10, 85, 30)
    3

    '''

    # calculate the minimum number of jumps
    travel_distance = finish_pos - start_pos

    if travel_distance % jumping_distance:
        return travel_distance / jumping_distance + 1
    else:
        return travel_distance / jumping_distance
