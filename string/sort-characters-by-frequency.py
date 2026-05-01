class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        buckets = [""] * (len(s) + 1)
    
        for val, freq in counts.items():
            buckets[freq] += val * freq

        return "".join(reversed(buckets))
        
        # bucket sort
        # T: O(N)
        # S: O(N)
        # Trade-off: uses memory for speed
        # Note: bucket size is bounded by len(s), 
        # but since input is alphabet only, at most 26 unique characters
        '''
        counts = Counter(s)
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        
        return "".join(val * freq for val, freq in sorted_counts)

        # Sorted
        # T: O(N log N) where N is unique chars
        # S: O(N)
        # Trade-off: uses speed for memory
        # Note: readability over speed (O(N log N) but simpler code)
        '''