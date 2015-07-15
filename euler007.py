# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 007 - 10001st prime

'''
Problem:

What is the Nth prime number?


Input:

First line contains T, and then the following T lines contain N
for the given test case.


Constraints:

1 <= T <= 10**3
1 <= N <= 10**4

'''

import math

# T test cases
cases = int(input())
nums = []

# Store all of the test case Ns in list nums
for case in list(range(cases)):
	nums.append(int(input()))

# Initialize list of primes and counters to run loop
primes = [0, 2]
count = 2
primecount = 1

# Create list of primes (the relatively brute force way)
while primecount < max(nums):
	flag = 0
	count += 1
	
	# check if each number is divisible by any numbers up to its root 
	for i in list(range(2,int(math.sqrt(count) + 1))):
		if count % i == 0:
			flag = 1
			break
	if flag == 0:
		primes.append(count)
		primecount += 1
    
# Print results for each case to screen    
for case in list(range(cases)):
	print(primes[nums[case]])