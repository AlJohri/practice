"""
A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given a zero-indexed array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Assume that:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""

# https://codility.com/demo/results/demo8JRBZT-TA5/

def solution(A):
    N = len(A)
    sum_upto_n_plus_1 = (N+1) * (N+2) // 2
    return sum_upto_n_plus_1 - sum(A)

# https://codility.com/demo/results/trainingVZAVSN-D9Q/

def solution(A):
    A.sort()
    for i, x in enumerate(A):
        if x != i+1:
            return i+1
    else:
        return len(A) + 1

assert solution([1]) == 2
assert solution([2, 1]) == 3
assert solution([2, 3, 1, 5]) == 4
