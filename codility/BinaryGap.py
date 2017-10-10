# https://codility.com/demo/results/training9G3VK4-MAP/

def solution(N):
    s = bin(N)[2:]

    max_length = 0
    start = None
    for i, x in enumerate(s):
        if x == "1" and start is None:
            start = i
        elif x == "1" and start is not None:
            current_length = i - start - 1 # not actually length, needs to be length in between
            max_length = max(max_length, current_length)
            start = i
        elif x == "0" and start is None:
            continue
        elif x == "0" and start is not None:
            continue
    return max_length

assert solution(9) == 2
assert solution(1041) == 5
