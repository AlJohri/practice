# https://codility.com/demo/results/trainingBK7HSN-CD9/

def solution(A):
    N = len(A)
    return 1 if sorted(A) == list(range(1, N+1)) else 0

assert solution([4, 1, 3, 2]) == 1
