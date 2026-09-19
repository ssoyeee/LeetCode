class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #binary search, O(logN)
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2

            #lucky case
            if target == nums[mid]:
                return mid
            
            if target>nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return l
            