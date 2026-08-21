class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums
        r = []

        for num in range(len(nums)-k+1):
            r.append(max(nums[num:num+k]))
        return r