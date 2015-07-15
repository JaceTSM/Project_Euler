# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 006 - Product Sum Difference

'''
Problem:

Find the difference between the sum of the squares of the first N 
natural numbers and the square of the sum.


Input:

First line contains T, and then the following T lines contain N
for the given test case.


Constraints:

1 <= T <= 10**4
1 <= N <= 10**4

'''

# T test cases
cases = int(input())
nums = []

# Store all of the test case Ns in nums
for case in list(range(cases)):
	nums.append(int(input()))

# Initialize the sum of squares and square of sums lists
sqsums = [1] 
sums = [1]

# for each value from 2 through the largest N, store all sums and squares
for i in list(range(2, max(nums) + 1)):
	sqsums.append(sqsums[-1] + i**2)
	sums.append(sums[-1] + i)

# print each solution to screen
for case in list(range(len(nums))):
	print(sums[nums[case] - 1]**2 - sqsums[nums[case] - 1])