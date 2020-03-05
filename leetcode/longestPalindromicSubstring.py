
class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = ""

        # Initalize empty matrix for dynamic programming solution
        n = len(s)
        matrix = [[None]*n for _ in range(n)]

        # Pre-populate 1 and 2 letter palindromes
        for i in range(n):
            matrix[i][i] = True
            longest = s[i:i+1]

        # Pre-populate 2 letter palindromes
        for i in range(n-1):
            matrix[i][i+1] = s[i] == s[i+1]
            if matrix[i][i+1]: longest = s[i:i+2]

        # Starting from 3-letter palindromes, fill in the matrix
        # for all length palindromes
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i+length-1
                matrix[i][j] = matrix[i+1][j-1] and s[i] == s[j]
                if matrix[i][j]: longest = s[i:j+1]
        
        return longest

