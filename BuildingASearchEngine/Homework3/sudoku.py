#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Sudoku http://en.wikipedia.org/wiki/Sudoku

# A valid sudoku square satisfies these two properties:

# 1. Each column of the square contains each of the numbers from 1 to n exactly once.
# 2. Each row of the square contains each of the numbers from 1 to n exactly once.

correct = [[1,2,3], 
           [2,3,1],
           [3,1,2]]
incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

# check a list whether has duplicate element
# using set
def has_duplicate(p):
    return len(p) != len(set(p))

# transpose a square matrix. In fact, python provide a build-in function zip()
def transpose(matrix):
    transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
    return transpose_matrix

# Define a procedure, check_sudoku, that takes as input a square list
# of lists representing an n x n sudoku puzzle solution and returns True
# if the input is a valid sudoku square and returns False otherwise

def has_duplicate_rows(square):
    for row in square:
        if has_duplicate(row):
            return True

def check_sudoku(square):
    # check rows
    if has_duplicate_rows((square)):
        return False
    
    # check columns
    #transpose_matrix = zip(*square)
    transpose_matrix = transpose(square)
    if has_duplicate_rows((transpose_matrix)):
        return False
    return True

if __name__ == "__main__":
    print correct
    print check_sudoku(correct)
    print incorrect
    print check_sudoku(incorrect)
    
        
    
