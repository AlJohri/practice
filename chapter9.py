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

# 9.3 A magic index in an array A[0.. .n-1] is defined to be an index such that A[i]
# = i. Given a sorted array of distinct integers, write a method to find a magic
# index, if one exists, in array A.
#
# FOLLOW UP
#
# What if the values are not distinct?

