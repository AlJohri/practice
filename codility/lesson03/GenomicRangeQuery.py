"""
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

def solution(S, P, Q)

that, given a non-empty zero-indexed string S consisting of N characters and two non-empty zero-indexed arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

The sequence should be returned as:

a Results structure (in C), or
a vector of integers (in C++), or
a Results record (in Pascal), or
an array of integers (in any other programming language).
For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Assume that:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
Complexity:

expected worst-case time complexity is O(N+M);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""

# https://codility.com/demo/results/demoNV524E-VMQ/

S, P, Q = ('CAGCCTA', [2, 5, 0], [4, 5, 6]) 

def slow_solution(S, P, Q):
    impact_map = {"A": 1, "C": 2, "G": 3, "T": 4}
    N = len(S)
    M = len(P)
    sequence_impact = [impact_map[nucleotide] for nucleotide in S]

    ret = []

    for K in xrange(M):
        start, end = P[K], Q[K]
        minimum_impact = min(sequence_impact[start:end+1])
        ret.append(minimum_impact)

    return ret


def fast_solution(S, P, Q):
    N, M = len(S), len(P)
    nucleotides = ["A", "C", "G", "T"]
    impact_map = {"A": 1, "C": 2, "G": 3, "T": 4}
    prefix_sum = {"A": [0] * (N+1), "C": [0] * (N+1), "G": [0] * (N+1), "T": [0] * (N+1)}

    # initialize prefix_sum to a vector of 1's corresponding to nuclueotide locations
    # leave index 0 empty for prefix sum
    for i, nucleotide in enumerate(S):
        prefix_sum[nucleotide][i+1] = 1

    # compute prefix_sum using vector of nuclueotide locations
    for i in xrange(1, N+1):
        for nucleotide in nucleotides:
            prefix_sum[nucleotide][i] += prefix_sum[nucleotide][i-1]

    ret = []

    # for each subsequence, check if nucleotide exists, from smallest nucleotide first
    for K in xrange(M):
        start, end = P[K], Q[K]
        for nucleotide in nucleotides:
            nucleotide_exists_in_slice = prefix_sum[nucleotide][end+1] - prefix_sum[nucleotide][start]
            if nucleotide_exists_in_slice > 0:
                ret.append(impact_map[nucleotide])
                break

    return ret

print(slow_solution(S, P, Q))
print(fast_solution(S, P, Q))
