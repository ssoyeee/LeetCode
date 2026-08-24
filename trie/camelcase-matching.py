class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # two pointer
        j = 0
        for ch in queries:
            if j < len(pattern) and ch == pattern[j]:
                j+=1
            elif ch.isupper():
                return False
        return j == len(pattern)