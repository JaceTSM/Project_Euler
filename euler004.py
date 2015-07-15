# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 004 - Largest Palindrome Product

'''
Problem:

Find the largest palindrome made from the product of two 3-digit numbers which is less than N.


Input:

First line contains T, and then the following T lines contain N
for the given test case.


Constraints:

1 <= T <= 100
101101 <= N <= 10**6

'''

import math

# Input T test cases and initialize lists that will hold the individual cases and all of the relevant palindromes 
cases = int(input())
maxnum = []
palindromes = [101101]

# Store each test case in maxnum
for case in list(range(cases)):
	maxnum.append(int(input()))
    
# Find all of the palindromes that are both products of two 3-digit numbers, and are smaller than N.
for i in range(100,int(math.sqrt(max(maxnum)))):
	for j in range(100,999):
		product = i*j
		if product > 101100 and product < max(maxnum):
			if str(product) == str(product)[::-1] and product not in palindromes:
				# Store the applicable numbers in palindromes
				palindromes.append(product)

# Add top-end constraint to palindromes to enable clean loop. Also sort the list.				
palindromes.append(1000000)
palindromes.sort()

# For each case, find the largest value in palindromes under N and print the results to screen
for case in list(range(len(maxnum))):
	for k in list(range(len(palindromes))):
		if palindromes[k] > maxnum[case]:
			print(palindromes[k-1])
			break