# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 057 - Square Root Convergents

'''
Problem:

It is possible to show that the square root of two can be expressed 
as an infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + 1/(2 + 1/(2 + ... = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 1.5
1 + 1/(2 + 1/2) = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth 
expansion, 1393985, is the first example where the number of digits in the 
numerator exceeds the number of digits in the denominator.

Given N. In the first N expansions, print the iteration numbers where the 
fractions contain a numerator with more digits than denominator.


Input:

Input contains an integer N


Output:

Print the answer corresponding to the test case.


Constraints:

8 <= N <= 10**4

'''

# Input n
num = int(input())

# We can look at each expansion as a ratio of p and q, which can be calculated
# every iteration. Initialize p and q here, and a counter for what expansion
# we are looking at.
p = 1
q = 1
xp = 0

# Iterate through each expansion, and each simplified fraction can be noted as:
# pnew = pold + 2*qold
# qnew = pold + qold
while xp < num:
    p, q = p + 2*q, p + q
    xp += 1

    # Whenever a numerator is longer than a denominator, print the expansion
    if len(str(p)) > len(str(q)):
        print(xp)