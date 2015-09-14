# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 015 - Lattice Paths

'''
Problem:

Starting in the top left corner of a 2×2 grid, and only being able to move 
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a N×M grid? As number of ways can be 
very large, print it modulo (10**9)+7.


Input:

The first line contains an integer T , i.e., number of test cases. 
Next T lines will contain integers N and M.


Constraints:

1 <= T <= 103
1 <= N <= 500
1 <= M <= 500

'''

import math

# Get T from user 
cases = int(input())

# For each case, get n and m from user
for case in list(range(cases)):
    n,m = list(map(int, input().split()))

    # The number of lattice paths for a grid is the binomal coefficient (n+m m) = (n + m)!/(m!(m + n - m)!)
    print((math.factorial(n + m)//(math.factorial(n) * math.factorial(m))) % 1000000007)