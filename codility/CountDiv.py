# https://codility.com/demo/results/trainingQKFMTK-G5M/

"""
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers
within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should
return 3, because there are three numbers divisible by 2 within
the range [6..11], namely 6, 8 and 10.

Assume that:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.

Complexity:

    - expected worst-case time complexity is O(1);
    - expected worst-case space complexity is O(1).
"""

import sys
import random

def solution(A, B, K):
    if A == B == 0:
        return 1
    A = max(A-1, 0)
    return B//K - A//K

assert solution(6, 11, 2) == 3
assert solution(11, 345, 17) == 20
assert solution(0, 0, 11) == 1
assert solution(1, 1, 11) == 0
print(solution(0, sys.maxsize, random.randint(1, sys.maxsize)))

# got 2000000000 expected 2000000001

# verify handling of range endpoints, multiple runs
# got 7 expected 8
# 1. 0.016 s OK
# 2. 0.016 s OK
# 3. 0.016 s OK
# 4. 0.016 s OK
# 5. 0.016 s WRONG ANSWER,  got 7 expected 8
# 6. 0.016 s WRONG ANSWER,  got 6 expected 7
