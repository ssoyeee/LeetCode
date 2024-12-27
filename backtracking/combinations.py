class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(prefix, nums, k):
            if k == 0:
                yield prefix
                return
            elif not nums:
                return
            yield from helper(prefix + [nums[0]], nums[1:], k-1)
            yield from helper(prefix, nums[1:], k)
        return list(helper([], list(range(1, n+1)), k)) # [1, 2, 3, 4, 5, ..., n]
    # n = 5, k = 3, [1 ,2, 3, 4, 5]
    # helper([], [1, 2, 3, 4, 5], 3)
    #   helper([1], [2, 3, 4, 5], 2)
    #       helper([1, 2], [3, 4, 5], 1)
    #           helper([1, 2, 3], [4, 5], 0)
    #       helper([1], [3, 4, 5], 2)
    #   helper([], [2, 3, 4, 5], 3)
    #       helper([2], [3, 4, 5], 2)
    #       helper([], [3, 4, 5], 3)
