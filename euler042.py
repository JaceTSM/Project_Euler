# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 042 - Coded Triangle Numbers

'''
Problem:

The nth term of a sequence of triangle numbers is given by, 
tn = (1/2)*n*(n+1)

so the first ten triangle numbers are: 
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

You are given an integer. If it is a triangular number tn, print the term n 
corresponding to this number, else print −1.


Input:

First line of input contains an integer T denoting the number of testcases. 
Each of the next T lines contains an integer.


Output:

Print the answer corresponding to each test case in a new line.


Constraints:

1 <= T <= 10**5 
1 <= tn <= 10**18

'''

# Input cases
cases = int(input())


# For each case, plug your input into the triangle number formula (as tn).
# If you get an integer as a result for n, then your number is a triangle number. 
for i in range(cases):
    num = int(input())

    # This is the equation above, but solved for n. (tri == n, num == tn)
    tri = (1/2)*((8*num +1)**(1/2) -1)
    
    # If it's a triangle number, print it, otherwise print -1.
    if tri % 1 == 0.0:
        print(int(tri))
    else:
        print(-1)