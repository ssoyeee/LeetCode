class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(prefix, nums):
            if not nums: 
                yield prefix
                return
            for index, num in enumerate(nums):
                yield from helper(prefix + [num], nums[:index] + nums[index+1:]) 
                # add num to prefix, all elements except the one at index
        return list(helper([], nums))
        
        # Time: O(N!*N)
        # Space: O(N!*N) The recursion stack depth is O(n), but since each call also creates a new sliced list of size up to O(n), the total auxiliary space becomes O(n^2). Including the output, which holds n! permutations of length n, the overall space complexity is O(n! * n)