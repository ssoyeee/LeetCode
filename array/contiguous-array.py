class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        for i in range(len(nums)):
            zero, one = 0, 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    zero += 1
                else:
                    one += 1
                if zero == one:
                    max_len = max(max_len, j-i+1)
        return max_len