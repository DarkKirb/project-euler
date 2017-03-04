#!/usr/bin/env python3
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?

spiral = [[1]]


def addRing():
    global spiral
    startval = spiral[0][-1] + 1
    currwidth = len(spiral)
    # Right side
    for i in range(currwidth):
        spiral[i].append(startval)
        startval += 1
    # Bottom side
    downlist = []
    for i in range(currwidth + 1):
        downlist.append(startval)
        startval += 1
    spiral.append(list(reversed(downlist)))
    # Left side
    for i in range(currwidth, -1, -1):
        spiral[i].insert(0, startval)
        startval += 1
    # Top side
    toplist = []
    for i in range(currwidth + 2):
        toplist.append(startval)
        startval += 1
    spiral.insert(0, toplist)

for i in range(500):
    addRing()

sum = -1  # 1 is counted twice.
for x in range(len(spiral)):
    y = 1000 - x
    sum += spiral[x][x]
    sum += spiral[x][y]
print(sum)
