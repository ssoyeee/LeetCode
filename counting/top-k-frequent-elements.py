from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums)
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        return [val for val, freq in sorted_counts[:k]]
        