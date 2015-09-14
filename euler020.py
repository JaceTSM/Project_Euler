# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 020 - Factorial Digit Sums

'''
Problem:

Find the sum of the digits in the number N!.


Input:

The first line contains an integer T , i.e., number of test cases. 
Next T lines will contain an integer N.


Output:

Print the values corresponding to each test case.


Constraints:

1 <= T <= 100 
1 <= N <= 10**4 

'''

import math

# Input number of cases
cases = int(input())

# For each case, take the factorial of the input, make it a string, map the string as a list of ints, sum the ints. Print.
for case in list(range(cases)):
    print(sum(map(int, list(str(math.factorial(int(input())))))))