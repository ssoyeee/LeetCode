class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')
        for index, value in enumerate(nums):
            window.append(value)
            if index < k-1:
                continue
            
            if current_max == float('-inf'):
                current_max = max(window)
            elif value > current_max:
                current_max = value
            results.append(current_max)

            if current_max == window.popleft():
                current_max = float('-inf')
        return results
        '''
        
        if not nums:
            return nums
        result = []

        for num in range(len(nums)-k+1):
            result.append(max(nums[num:num+k]))
        return result

        # brute-force
        # T: O(N) - we have to calculate max value of window everytime we move

      # idea: maintain current max while sliding the window.
              compare new value with current max and update if larger.
              only rescan the window to recompute max when the old max falls out of the window bounds.
              '''