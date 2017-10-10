# https://codility.com/demo/results/trainingPYFJ7R-V57/

def solution(A, K):
    N = len(A)
    if N == 0:
        return A
    K = K % N
    B = [0] * N
    for i, x in enumerate(A):
        index = (i + K) % N
        B[index] = x
    return B

assert solution([3, 8, 9, 7, 6], 1) == [6, 3, 8, 9, 7]
assert solution([], 1) == []
