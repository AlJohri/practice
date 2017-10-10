"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty zero-indexed array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty zero-indexed array A consisting of M integers, returns a sequence of integers representing the values of the counters.

The sequence should be returned as:

a structure Results (in C), or
a vector of integers (in C++), or
a record Results (in Pascal), or
an array of integers (in any other programming language).
For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Assume that:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
Complexity:

expected worst-case time complexity is O(N+M);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""

# https://codility.com/demo/results/demo6KPS7K-87N/

N, A = (5, [3, 4, 4, 6, 1, 4, 4])

def slow_solution(N, A):
    counters = [0] * N
    for K,X in enumerate(A):
        if 1 <= X <= N: counters[X-1] += 1
        elif A[K] == (N + 1): counters = [max(counters)] * N
    return counters

def slow_solution2(N, A):
    counters = [0] * N
    max_counter = 0
    for K,X in enumerate(A):
        if 1 <= X <= N:
            counters[X-1] += 1
            max_counter = max(max_counter, counters[X-1])
        elif A[K] == (N + 1):
            counters = [max_counter] * N
    return counters

def slow_solution3(N, A):
    TRUE_SWITCHES = [True] * N
    switches = [False] * N
    counters = [0] * N
    max_counter = 0

    for K,X in enumerate(A):
        if 1 <= X <= N:
            if switches[X-1] == True:
                counters[X-1] = switch_max_counter + 1
                switches[X-1] = False
            else:
                counters[X-1] += 1
            max_counter = max(max_counter, counters[X-1])
        elif A[K] == (N + 1):
            switches = TRUE_SWITCHES[:]
            switch_max_counter = max_counter

    for i, switch in enumerate(switches):
        if switch == True:
            counters[i] = switch_max_counter

    return counters


def fast_solution(N, A):
    counters = [0] * N
    max_counter = 0
    last_update = 0

    for K,X in enumerate(A): # O(M)
        if 1 <= X <= N:
            counters[X-1] = max(counters[X-1], last_update)
            counters[X-1] += 1
            max_counter = max(counters[X-1], max_counter)
        elif A[K] == (N + 1):
            last_update = max_counter

    for i in xrange(N): # O(N)
        counters[i] = max(counters[i], last_update)

    return counters

print(slow_solution(N, A))
print(slow_solution2(N, A))
print(slow_solution3(N, A))
print(fast_solution(N, A))

assert fast_solution(5, [3, 4, 4, 6, 1, 4, 4]) ==  [3, 2, 2, 4, 2]
