# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 002 - Even Fib Sum

'''
Problem:

For input N, find the sum of all even-valued Fibonacci numbers below N.


Input:

First line contains T, and then the following T lines contain N
for the given test case.


Constraints:

1 <= T <= 10**5
1 <= N <= 4 * 10**16

'''

# Input T cases
cases = int(input())

for case in list(range(cases)):
	total = 0
	fib = [0,1]
	# Input N for given case
	num = int(input())

	# Calculate Fibonacci sequence up to N and sum all of the even numbers
	while fib[1] < num:
		if fib[1] % 2 == 0:
			total += fib[1]
		temp = fib[0] + fib[1]
		fib[0] = fib[1]        
		fib[1] = temp

	# Print results of case to screen
	print(total)