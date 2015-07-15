# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 008 - Largest Product in a Series

'''
Problem:

Find the greatest product of K consecutive digits in an N digit number

Input:

First line contains T that denotes the number of test cases. 
First line of each test case will contain two integers N & K.
Second line of each test case will contain a N digit integer.

Constraints:

1 <= T <= 100
1 <= K <= 7
K <= N <= 1000

'''

import functools

# T test cases
cases = int(input())

for case in list(range(cases)):
	
	# Gather N (length) and K (run) for a given case, and then N (num)
	length, run = map(int, input().split())
	num = input()
	sums = []
	
	# Loop through the number and multiply the digits in the length of the run.
	for i in list(range(run, length + 1)):
		sums.append(functools.reduce(lambda x, y: x*y, map(int, num[i - run:i])))
	
	# Print the results to screen
	print(max(sums))