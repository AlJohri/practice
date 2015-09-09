"""
A non-empty zero-indexed array A consisting of N integers is given. The first covering prefix of array A is the smallest integer P such that 0≤P<N and such that every value that occurs in array A also occurs in sequence A[0], A[1], ..., A[P].

For example, the first covering prefix of the following 5−element array A:

A[0] = 2
A[1] = 2
A[2] = 1
A[3] = 0
A[4] = 1
is 3, because sequence [ A[0], A[1], A[2], A[3] ] equal to [2, 2, 1, 0], contains all values that occur in array A.

Write a function

def solution(A)

that, given a zero-indexed non-empty array A consisting of N integers, returns the first covering prefix of A.

For example, given array A such that

A[0] = 2
A[1] = 2
A[2] = 1
A[3] = 0
A[4] = 1
the function should return 3, as explained above.

Assume that:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [0..N−1].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""

# Alpha 2010
# https://codility.com/media/train/solution-prefix-set.pdf

def slow_solution(A):
    num_unique_values = len(set(A))

    values_thus_far = []
    num_unique_values_thus_far = 0

    for i, number in enumerate(A):
        if number not in values_thus_far:
            values_thus_far.append(number)
            num_unique_values_thus_far += 1

        if num_unique_values_thus_far == num_unique_values:
            return i

def slow_solution2(A):
    values_thus_far = []
    num_unique_values_thus_far = 0
    unique_values_index = {}

    for index, number in enumerate(A):
        if number not in values_thus_far:
            values_thus_far.append(number)
            num_unique_values_thus_far += 1
            unique_values_index[num_unique_values_thus_far] = index

    return unique_values_index[num_unique_values_thus_far]

def fast_solution(A):
    unique_values_thus_far = {}
    unique_values_index = {}

    for index, number in enumerate(A):
        if number not in unique_values_thus_far:
            unique_values_thus_far[number] = True
            unique_values_index[len(unique_values_thus_far)] = index

    return unique_values_index[len(unique_values_thus_far)]

A = [2, 1, 0, 1]

print(slow_solution(A))
print(slow_solution2(A))
print(fast_solution(A))
