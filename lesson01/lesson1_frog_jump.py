#!/usr/bin/env python
# encoding: utf-8


# Lesson 1 - Time Complexity - FrogJmp
# https://codility.com/demo/take-sample-test/frog_jmp


def solution(X, Y, D):
    '''
    This function takes start and finish positions.
    Calculates how many jumps are needed to get there.

    (int, int, int) -> int
    
    
    >>> solution(10, 85, 30)
    3
    
    '''
    
    
    # declare variables
    min_jumps = 0
    foo = 0
    
    
    # calculate the minimum number of jumps
    if Y > X:
        foo = (Y - X) / D
        
        if ((Y - X) % D) != 0:
            min_jumps = foo + 1
        
        else:
            min_jumps = foo
    
    else:
        return 0
    
    
    # return the result
    return min_jumps