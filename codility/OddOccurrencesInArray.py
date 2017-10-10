# https://codility.com/demo/results/trainingYU5D45-WMT/

def solution(A):
    A.sort()
    i = 0
    while i < len(A) - 1:
        if A[i] == A[i+1]:
            i += 2
            continue
        else:
            return A[i]
    else:
        if A[i] != A[i-1]:
            return A[i]
        else:
            return None

assert solution([9, 3, 9, 3, 9, 7, 9]) == 7
assert solution([2, 1, 1, 1, 1, 1, 1]) == 2
assert solution([1, 1, 1, 1, 1, 1, 1]) == None
