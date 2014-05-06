#!/usr/bin/env python
# encoding: utf-8


# Lesson 3 - Prefix Sums - Genomic Range Query
# https://codility.com/demo/take-sample-test/genomic_range_query

# got 75% when evaluated(60% correctness, 100% performance)
# dunno why but it fails on 'simple tests'


def solution(S, P, Q):
    '''
    Find the smallest impact factor for sequences of DNA ranges.


    >>> solution('CAGCCTA', [2, 5, 0], [4, 5, 6])
    [2, 4, 1]
    
    '''
    

    # declare variables
    N = len(S)
    M = len(P)
    DNA_prefix_sums = [0] * N
    impact_factors = [0] * M
    n_nucleotides = len(DNA.keys())
    nucleotides = [0] * n_nucleotides
    DNA = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4
    }


    # calculate the sum prefix of nucleotides occurences
    for i, nucleotide in enumerate(S):
        nucleotides[DNA[nucleotide] - 1] += 1
        DNA_prefix_sums[i] = [0] * n_nucleotides

        for j in xrange(n_nucleotides):
            DNA_prefix_sums[i][j] = nucleotides[j]


    # calculate impact factors
    for i in xrange(M):
        # if the sequence point at specific nucleotide, not a range
        if P[i] == Q[i]:
            impact_factors[i] = DNA[S[P[i]]]

        # if the sequence points at a DNA range
        else:
            nucleotides = [0] * n_nucleotides

            # calculate total nucleotides difference
            for j in xrange(n_nucleotides):
                nucleotides[j] = DNA_prefix_sums[Q[i]][j] - DNA_prefix_sums[P[i]][j]

            # find the smallest nucleotide 
            for j, nucleotide in enumerate(nucleotides):
                if nucleotide > 0:
                    impact_factors[i] = j + 1
                    break


    # return an array of M integers containing impact factors
    return impact_factors


# my first attempt, O(N * M) solution(100% correct though)
def long_solution(S, P, Q):
    '''
    Find the smallest impact factor for sequences of DNA ranges.


    >>> solution('CAGCCTA', [2, 5, 0], [4, 5, 6])
    [2, 4, 1]
    
    '''
    

    # declare variables
    N = len(S)
    M = len(P)
    current_sum = 0
    DNA_prefix_sums = [0] * N
    impact_factors = [0] * M
    DNA = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4
    }


    # calculate impact factors for each P[i] and Q[i]
    for i in xrange(M):
        lowest_impact_factor = 4

        for j in xrange(P[i], Q[i] + 1):
            if lowest_impact_factor > DNA[S[j]]:
                lowest_impact_factor = DNA[S[j]]

            if lowest_impact_factor == 1:
                break

        impact_factors[i] = lowest_impact_factor


    # return an array of M integers containing impact factors
    return impact_factors