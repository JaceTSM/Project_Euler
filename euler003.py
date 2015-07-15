# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 003 - Largest Prime Factor

'''
Problem:

What is the largest prime factor for a given number N.


Input:

First line contains T, and then the following T lines contain N
for the given test case.


Constraints:

1 <= T <= 10
1 <= N <= 10**12

'''

import math

# Input T cases
cases = int(input())

# For each case, find the factors of input N.
for case in list(range(cases)):
	num = int(input())
	factors = [num]
	
	# only search for factors up to the square root of a number.
	for i in list(range(2,(int(math.sqrt(num)) + 1))):
		while factors[-1] % i == 0:
			factors.append(factors[-1]//i)
			factors[-2] = i
	
	# Print case result to screen
	print(max(factors))