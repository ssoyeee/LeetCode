class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        max_freq=0
        for r in range(len(nums)):
            cost = nums[r]*(r-l+1)-sum(nums[l:r+1])
            while cost > k:
                l+=1
                cost = nums[r]*(r-l+1)-sum(nums[l:r+1])
            if cost <= k:
                max_freq = r-l+1
        return max_freq
            