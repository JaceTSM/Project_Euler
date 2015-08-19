# !/Python34
# Copyright 2015 Tim Murphy. All rights reserved.

# Project Euler 011 - Prime Summation

'''
Problem:

Given a 20x20 grid of integers, find the greatest product of 4 integers in a line.
A line consists of any 4 numbers in a row, column, or diagonal.

Input:

Twenty lines of twenty integers each.

Constraints:

0 <= Each integer on the grid <= 100

'''

grid = []
products = []

# Generate grid from user
for i in range(0,20):
	grid += [list(map(int, input().split()))]

# Vertical products
for row in range(len(grid) - 3):
	for column in range(len(grid[row])):
		products += [ grid[row][column] * grid[row + 1][column] * grid[row + 2][column] * grid[row + 3][column] ]

# Horizontal products
for row in range(len(grid)):
	for column in range(len(grid[row]) - 3):
		products += [ grid[row][column] * grid[row][column + 1] * grid[row][column + 2] * grid[row][column + 3] ]

# Diagonal (Top left to bottom right) products
for row in range(len(grid) - 3):
	for column in range(len(grid[row]) - 3):
		products += [ grid[row][column] * grid[row + 1][column + 1] * grid[row + 2][column + 2] * grid[row + 3][column + 3] ]

# Diagonal (Top right to bottom left) products
for row in range(len(grid) - 3):
	for column in range(3, len(grid[row])):
		products += [ grid[row][column] * grid[row + 1][column - 1] * grid[row + 2][column - 2] * grid[row + 3][column - 3] ]

print(max(products))

