from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counted_nums = Counter(nums)
        sorted_counts = sorted(counted_nums.items(), key=lambda x: (-x[1], x[0]))
        return [val for val, freq in sorted_counts[:k]]
        