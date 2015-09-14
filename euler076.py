# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 076 - Counting Summations

'''
Problem:

It is possible to write five as a sum in exactly six different ways:

4+1
3+2
3+1+1
2+2+1
2+1+1+1
1+1+1+1+1

How many different ways can N be written as a sum of at least two positive integers?

As answer can be large, print %(10**9+7)


Input:

First line of the input contains T, which is number of testcases. 
Each testcase contains N.


Constraints:

1 <= T <= 100 
2 <= N <= 1000


Output Format:

Print the output corresponding to each testcase on a new line.

'''


# This is my implementation of the partition function
# Learn more about it here: https://en.wikipedia.org/wiki/Partition_(number_theory)#Generating_function
def p(k, plist):
	sum = 0
	
	# p(-|x|) = 0
	if k < 0:
		return(0)
	
	# p(0) = 1
	if k == 0:
		return(1)
	
	# p(|x|) is recursive	
	for i in list(range(1, k + 1)):
		m = (i*(3*i - 1))//2
		m2 = ((-i)*(-3*i - 1))//2
		sign = -((-1)**i)
		
		if k - m < 0:
			break
		
		if k - m == 0:
			sum += 1*sign
			break
		
		if k - m >= 1:
			try:
				sum += plist[k - m]*sign
			except IndexError:
				sum += p(k - m, plist)*sign
			
		if k - m2 < 0:
			break
		
		if k - m2 == 0:
			sum += 1*sign
			break
			
		if k - m2 >= 1:
			try:
				sum += plist[k - m2]*sign
			except IndexError:
				sum += p(k - m2, plist)*sign
		
		
	if sum > plist[-1]:
		plist.append(sum)
	return(sum)
		
	
# This problem is a modification of the classic 'coin piles' problem,
# so we shall think about it as if we were looking at coins and
# dividing them in to piles

# Initialize a pile count, list of piles, and input number of cases
piles = 0
cases = int(input())
plist = [1, 1]

# For each case, input the number of coins you want to divide into piles
for i in list(range(cases)):
	coins = int(input())
	
	# Our partition function is recursive, and python only can recurse about 1000 levels,
	# I have it solve it in 500 level chunks. I'll rewrite this with a memoization function soon. 
	try:
		piles = plist[coins]
	except IndexError:
		if coins > 500:
			num = coins // 500
			for j in list(range(1,num + 1)):
				p(500*j, plist)
			p(coins, plist)
		piles = p(coins, plist)

	# Print how many piles we count, mod (10**9) + 7
	print((piles - 1) % 1000000007)