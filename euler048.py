# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 048 - Self Powers
'''
Problem:

The series,
 
1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317

Find the last ten digits of the series,

1**1 + 2**2 + 3**3 + ... + N**N

Note: You do not need to print leading zeros.


Input:

Input contains an integer N


Output:

Print the answer corresponding to the test case.


Constraints:

1 <= N <= 2*(10**6)

'''

# Input your integer n, initialize a total
num = int(input())
total = 0

# For each number i from 1 to n, add (i**i % 10**10) to total
# When adding these large numbers, the leading digits don't matter 
for i in range(1, num + 1):
    total += pow(i,i,10000000000)
    
# Print, mod 10**10
print(total % 10000000000)