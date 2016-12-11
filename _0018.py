#!/usr/bin/env python3
# cython: language_level=3
#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#That is, 3 + 7 + 4 + 9 = 23.
#Find the maximum total from top to bottom of the triangle below:
triangle=[
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
#NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
def greedy(line, row):
    if line == 14:
        return triangle[line][row]
    global triangle
    print("Value at",line,",",row,":",triangle[line][row])
    left,right=triangle[line+1][row],triangle[line+1][row+1]
    print("Value at left child:",left)
    print("Value at right child:",right)
    if left==right:
        print("Peeking forward.")
        if line == 13:
            print("Neither of the children have children. choosing left.")
            return triangle[line][row]+greedy(line+1,row)
        left=max(triangle[line+2][row],triangle[line+2][row+1])
        right=max(triangle[line+2][row+1],triangle[line+2][row+2])
        print("Left child has children: ",(triangle[line+2][row],triangle[line+2][row+1]))
        print("Right child has children: ",(triangle[line+2][row+1],triangle[line+2][row+1]))
    if left > right:
        print("Going left...")
        return triangle[line][row]+greedy(line+1,row)
    print("Going right...")
    return triangle[line][row]+greedy(line+1,row+1)
def bruteforce(line, row):
    if line == 14:
        return triangle[line][row]
    val=max(bruteforce(line+1,row),bruteforce(line+1,row+1))
    val+=triangle[line][row]
    return val
print(greedy(0,0))
print(bruteforce(0,0))
