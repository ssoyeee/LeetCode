class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        sentence = []
        for c in s:
            if c.isalnum():
                sentence.append(c.lower())

        left = 0
        right = len(sentence)-1
        
        while left<right:
            if sentence[left] == sentence[right]:
                left += 1
                right -= 1
            else:
                return False            
        return True    
        # Time: O(n) -- where n is length of s, one pass with two pointers to compare O(n)+ one pass to clean the string O(n)
        # Space: O(n) -- sentence list