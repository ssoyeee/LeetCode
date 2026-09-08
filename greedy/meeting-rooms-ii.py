import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        heap = []
        for start, end in intervals:
            if heap and heap[0] <= start: #room is already free
                heapq.heapreplace(heap, end)
            else: # new room is needed, push a new room with new end time
                heapq.heappush(heap, end)    
        return len(heap)
        # Time: O(N log N) -- sort() is O(n log n); each heap operation is O(log n), done n times
        # Space: O(n) -- in the worst case, heap size could be n