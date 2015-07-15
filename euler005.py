# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 005 - Smallest Multiple

'''
Problem:

What is the smallest positive number that is evenly divisible(divisible with no remainder) 
by all of the numbers from 1 to N?

Input:

First line contains T, and then the following T lines contain N
for the given test case.


Constraints:

1 <= T <= 10
1 <= N <= 40

'''

import math

# Returns a list of all least prime factors of num (and 1)
def factorize(num):
	factors = [num]
	for i in list(range(2,(int(math.sqrt(num)) + 1))):
		while factors[-1] % i == 0:
			factors.append(factors[-1]//i)
			factors[-2] = i
	return factors
	
# Returns the greatest common denominator of a and b
def gcd(a,b):
	remainder = 1
	while remainder != 0:
		remainder = a % b
		a = b
		b = remainder
	return a
	
# Returns the least common multiple of a and b
def lcm(a,b):
	return ((a*b)//gcd(a,b))

# Input T cases
cases = int(input())

# For each case N, find the lcm of all numbers 2 through N, and print results to screen
for case in list(range(cases)):
	total = 1
	n = int(input())
	for i in list(range(2,n+1)):
		total = lcm(total, i)
	print(total)