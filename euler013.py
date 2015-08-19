# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 013 - Large Sum

'''
Problem:

Work out the first ten digits of the sum of N 50-digit numbers.


Input:

First line contains N, next N lines contain a 50 digit number each.


Output:

Print only first 10 digit of the final sum


Constraints:

1 <= N <= 10**3

'''

# Acquire number of inputs
inputs = int(input())
nums = []

# Acquire each number to add
for i in range(inputs):
	nums += [int(input())]

# Sum the inputs
total = sum(nums)

# Print the first 10 digits of the sum
print(str(total)[0:10])

