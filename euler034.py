# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 034 - Digit Factorials

'''
Problem:

19 is a curious number, as 1! + 9! = 1 + 362880 = 362881 which is divisible by 19.

Find the sum of all numbers below N which divide the sum of the factorial of their digits.

Note: as 1!,2!, ... 9! are not sums they are not included.


Input:

Input contains an integer N


Output:

Print the answer corresponding to the test case.


Constraints:

10 <= N <= 10**5

'''

import math

# Input n, initialize nums list to store all numbers which divide the sum of the factorial of their digits
n = int(input())
nums = []

# For each number 10 to n, test for the trait in question
for i in range(10, n):
    digits = list(map(int, str(i)))
    
    for j in range(len(digits)):
        digits[j] = math.factorial(digits[j])
    facsum = sum(digits)
    if facsum % i == 0:
        nums += [i]
        
# Print results
print(sum(nums))