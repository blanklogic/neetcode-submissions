class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def helper(l, r): # check for palindromes
            nonlocal res, resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            helper(i, i) # odd palindromes
            helper(i, i + 1) # even palindromes
        return res