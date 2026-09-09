class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        max_freq = 0
        window_sum = 0
        for r in range(len(nums)):
            window_sum += nums[r]
            cost = nums[r]*(r-l+1) - window_sum
            while cost > k:
                window_sum -= nums[l]
                l += 1
                cost = nums[r]*(r-l+1) - window_sum
            if cost <= k:
                max_freq = max(max_freq, r-l+1)
        return max_freq
        
        # Time: O(n log n) -- sort() is O(n log n), sliding window(for+while) is O(n); O(n log n)
        # Space: O(1) -- three int variables, sort() is in-place