# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 001 - Multiples of 3 and 5

'''
Problem:

For T test cases, sum all of the multiples of 3 and 5 below N.


Input:

First line contains T, and then the following T lines contain N
for the given test case.


Constraints:

1 <= T <= 10**5
1 <= N <= 10**9

'''

# cases is T from the problem statement.
cases = int(input())

# For each case, solve the problem
for case in list(range(cases)):

	# For each case, your sum is equal to the average of all multiples of 3 and 5 below N, minus the sum of all multiples of 15
	n = int(input())
	total = ((3 + (((n-1)//3)*3))*((n-1)//3)//2) + ((5 + (((n-1)//5)*5))*((n-1)//5)//2) - ((15 + (((n-1)//15)*15))*((n-1)//15)//2)

	# For each case, print the solution to screen
	print(total)