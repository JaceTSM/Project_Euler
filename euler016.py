# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 016 - Power Digit Sums

'''
Problem:

2**9 = 512 and the sum of its digits is 5 + 1 + 2 = 8.

What is the sum of the digits of the number 2**N?


Input:

The first line contains an integer T , i.e., number of test cases. 
Next T lines will contain an integer N.


Output:

Print the values corresponding to each test case.


Constraints:

1 <= T <= 100 
1 <= N <= 10**4 

'''

# Input number of cases, initialize list of cases
cases = int(input())
nums = []

# Input cases, store them in nums
for case in list(range(cases)):
    nums += [int(input())]
    
# For each case, square the number, make it a string, map the string as a list of ints, and then sum the list. Print it.
for num in nums:
    print(sum(list(map(int, str(2**num)))))