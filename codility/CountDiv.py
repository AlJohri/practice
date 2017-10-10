# https://codility.com/demo/results/trainingQKFMTK-G5M/

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
