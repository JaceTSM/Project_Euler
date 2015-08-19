# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 010 - Prime Summation

'''
Problem:

The sum of the primes below 10 is 2+3+5+7=17.

Find the sum of all the primes not greater than given N.

Input:

First line contains T, and then the following T lines contain N
for the given test case.

Constraints:

1 <= T <= 10000
1 <= N <= 1000000

'''


import math

cases = int(input())
nums = []
primes = []
sums = [ 0, 0 ]

for case in list(range(cases)):
    nums.append(int(input()))

## Sieve of Eratosthenes

# Truth is the list of whether each integer is prime or not. 0 and 1 are not prime, so they are false.
maxprime = 1000003
truth = [False, False] + [True]*(maxprime - 1)

# Use the sieve to mark all of the non-primes false.
for j in list(range(int(math.sqrt(len(truth))) + 1)):
    if truth[j]:
        cut = j**2
        while cut <= maxprime:
            truth[cut] = False
            cut += j

# Make an array where each index is the solution for it's given input
for k in list(range(len(truth))):
    if truth[k]:
        primes.append(k)
        if k > 2:
            sums += (k - primes[-2])*[primes[-2] + sums[-1]]

# Print solutions
for case in list(range(cases)):
    print(sums[nums[case]])