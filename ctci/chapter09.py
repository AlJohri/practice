# 9.1 A child is running up a staircase with n steps, and can hop either 1 step, 2 steps,
# or 3 steps at a time. Implement a method to count how many possible ways the
# child can run up the stairs.

def checkSteps(n):
	if n < 0: return 0
	elif n == 0: return 1
	else:
		return checkSteps(n-3) + checkSteps(n-2) + checkSteps(n-1)

print "checkSteps"
print "0", checkSteps(0)
print "1", checkSteps(1)
print "2", checkSteps(2)
print "3", checkSteps(3)
print "4", checkSteps(4)
print "5", checkSteps(5)
print ""

# 9.2 Imagine a robot sitting on the upper left corner of an X by Y grid. The robot can
# only move in two directions: right and down. How many possible paths are there
# for the robot to go from (0,0) to (X,Y)?
#
# FOLLOW UP
#
# Imagine certain spots are "off limits," such that the robot cannot step on them.
# Design an algorithm to find a path for the robot from the top left to the bottom
# right.

from math import factorial

def possiblePaths(x, y):
	return factorial(x+y) / (factorial(x) * factorial(y))

def possiblePaths2(finalX, finalY, curPos=[0,0]):
	# print curPos
	if (curPos[0] > finalX) or (curPos[1] > finalY): return 0
	elif curPos == [finalX, finalY]: return 1
	else:
		return possiblePaths2(finalX, finalY, [curPos[0]+1, curPos[1]]) + possiblePaths2(finalX, finalY, [curPos[0], curPos[1]+1])

print "possiblePaths"
print "0,0", possiblePaths(0,0)
print "3,3", possiblePaths(3,3)
print "4,2", possiblePaths(4,2)
print ""

print "possiblePaths2"
print "0,0", possiblePaths2(0,0)
print "3,3", possiblePaths2(3,3)
print "4,2", possiblePaths2(4,2)
print ""

# 9.3 A magic index in an array A[0...n-1] is defined to be an index such that A[i]
# = i. Given a sorted array of distinct integers, write a method to find a magic
# index, if one exists, in array A.
#
# FOLLOW UP
#
# What if the values are not distinct?

def findMagicIndex(A):
	for i, a in enumerate(A):
		if i == a: return i
	return -1

def findMagicIndex2(A, indicies=None):
	if indicies == None: indicies = [x for x in range(len(A))]

	if len(A) == 0: return -1
	mid = len(A)/2

	if len(A) == 1: return -1

	if A[mid] == indicies[mid]:
		return indicies[mid]
	elif A[mid] < indicies[mid]:
		return findMagicIndex2(A[mid:], indicies[mid:]) # right
	else:
		return findMagicIndex2(A[:mid], indicies[:mid]) # left

# works with duplicates
def findMagicIndex3(A, indicies=None):
	if indicies == None: indicies = [x for x in range(len(A))]

	if len(A) == 0: return -1
	mid = len(A)/2

	if A[mid] == indicies[mid]:
		return indicies[mid]

	if len(A) == 1: return -1

	min_left = min(A[mid], mid)
	left = findMagicIndex3(A[:min_left], indicies[:min_left])
	if left > -1: return left

	right = findMagicIndex3(A[mid:], indicies[mid:])
	return right


print "findMagicIndex"
print "[-40,-20,-1,1,2,3,5,7,9,12,13]", findMagicIndex([-40,-20,-1,1,2,3,5,7,9,12,13])
print ""

print "findMagicIndex2"
print "[-40,-20,-1,1,2,3,5,7,9,12,13]", findMagicIndex2([-40,-20,-1,1,2,3,5,7,9,12,13])
print ""

print "findMagicIndex3 (with duplicates)"
print "[-40,-20,-1,1,2,3,5,7,9,12,13]", findMagicIndex3([-40,-20,-1,1,2,3,5,7,9,12,13])
print "[-10,-5,2,2,2,3,4,7,9,12,13]", findMagicIndex3([-10,-5,2,2,2,3,4,7,9,12,13])
print ""

# 9.4 Write a method to return all subsets of a set.

from itertools import combinations

def powerset(A):
	return reduce(lambda x,y: x+y, [list(combinations(A, i)) for i in range(len(A)+1)], [])

print "powerset([1,2,3,4])", powerset([1,2,3,4])
print ""

# 9.5 Write a method to compute all permutations of a string

from itertools import permutations

def getPerms(str):
	return ["".join(x) for x in list(permutations(str, len(str)))]

print "getPerms(hello)", getPerms("hello")
print ""

# 9.6 Implement an algorithm to print all valid (i.e., properly opened and closed) combinations
# of n-pairs of parentheses.

def validParens(str):
	pass

# 9.7 Implement the "paint fill" function that one might see on many image editing
# programs. That is, given a screen (represented by a two-dimensional array of colors),
# a point, and a new color, fill in the surrounding area until the color changes from the
# original color.

# 9.8 Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents)
# and pennies (1 cent), write code to calculate the number of ways of representing n
# cents.

# http://rosettacode.org/wiki/Count_the_coins#Simple_version
# https://bitbucket.org/trebsirk/algorithms/src/c6d9df11e0be2695ab941418ba7660656f4c189e/coinchanging.py?at=master

def numWaysToMakeChange(amount, coins=[1, 5, 10, 25]):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in xrange(coin, amount + 1):
            ways[j] += ways[j - coin]
    return ways[amount]

print "numWaysToMakeChange(5): ", numWaysToMakeChange(5)
print "numWaysToMakeChange(6, [5, 10, 25]): ", numWaysToMakeChange(6, [5, 10, 25])
print "numWaysToMakeChange(20): ", numWaysToMakeChange(20)
print "numWaysToMakeChange(25): ", numWaysToMakeChange(25)
print "numWaysToMakeChange(100): ", numWaysToMakeChange(100)
print ""



# 9.9 Write an algorithm to prim all ways of arranging eight queens on an 8x8 chess
# board so that none of them share the same row, column or diagonal. In this case,
# "diagonal" means all diagonals, not just the two that bisect the board.

# 9.10 You have a stack of n boxes, with widths w1, heights h1, and depths d1. The boxes
# cannot be rotated and can only be stacked on top of one another if each box in the
# stack is strictly larger than the box above it in width, height, and depth. Implement
# a method to build the tallest stack possible, where the heigh t of a stack is the sum of
# the heights of each box.

# 9.11 Given a boolean expression consisting of the symbols 0, 1, &, |, and ^, and a desired
# boolean result value result, implement a function to count the number of ways of
# parenthesizing the expression such that it evaluates to result.



