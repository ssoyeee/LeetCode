class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict) 
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True # empty string is always considered valid (Base case)

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # once dp[i] is confirmed True, further j's won't change the result
        
        return dp[n]

        # T: O(n^2) - O(n^3) when we may include creating substring 's[j:i]'
        # S: O(n+m) - dp array + wordSet 