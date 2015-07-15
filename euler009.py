# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 009 - Special Pythagorean Triplet

'''
Problem:

Given N, Check if there exists any Pythagorean triplet for which a+b+c=N 
Find maximum possible value of abc among all such Pythagorean triplets, 
If there is no such Pythagorean triplet print −1.

Input:

First line contains T, and then the following T lines contain N
for the given test case.

Constraints:

1 <= T <= 3000
1 <= N <= 3000

'''

# T test cases
cases = int(input())

# For each case, input number N
for case in list(range(cases)):
	products = []
	n = int(input())
	
	# Find Pythagorean triplets that fulfill the conditions (some algebra was necessary)
	for b in list(range(1,n//3)):
		a = (n**2 - 2*n*b)/(2*n - 2*b)
		if a % 1 == 0.0:
			a = int(a)
			c = ((a**2 + b**2)**(1/2))
			if c % 1 == 0.0:
				if a != b:
					# Generate a list of the Pythagorean triplet products
					products.append(a*b*c)
	
	# If there is valid triplet, print the largest product, otherwise print '-1'
	if len(products) > 0:
		print(int(max(products)))
	else:
		print(-1)