"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. A
zero-indexed array A of N non-negative integers, specifying the radiuses of the
discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0

https://codility-frontend-prod.s3.amazonaws.com/media/task_img/number_of_disc_intersections/media/auto/mpaecfada7c1e52a7b01b04916c859b15d.png

There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].
Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""

# https://codility.com/demo/results/demoG37S7P-R37/

# Helpful StackOverflow Links:
# abstract solution: http://stackoverflow.com/a/4801275
# python solution: http://stackoverflow.com/a/26138026

from bisect import bisect

def solution(A):

    N = len(A)
    pairs = 0

    discs_sorted_by_left_side = sorted((x-r,x+r) for x, r in enumerate(A))
    starts = [i[0] for i in discs_sorted_by_left_side]

    for i, (left_side, right_side) in enumerate(discs_sorted_by_left_side):

        # For the current interval, do a binary search to see where the right end point of the
        # interval (i.e. i+A[i]) will go (called the rank). Now you know that it intersects all
        # the elements to the left.

        count = bisect(starts, right_side)

        # For disk i, i disks that start to the left have already been dealt with.
        # Thus, subtract current position (i) to exclude previous matches.
        # Subtract one more to prevent counting the disk it self.
        # We don't want to double count intervals and self intersections.

        count -= (i+1)
        pairs += count
        if pairs > 10000000: return -1

    return pairs
