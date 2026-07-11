class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = {}
        # res, maxCount = 0, 0

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        #     res = n if count[n] > maxCount else res
        #     maxCount = max(count[n], maxCount)
        # return res
       
        # hashmap
        # count = {}
        # for n in nums:
        #     count[n] = 1 +count.get(n, 0)
        #     if count[n] > len(nums)//2:
        #         return n
        
        #boyer-moore algorithm
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n #set the first number as majority number firstly
            count+=(1 if n==res else -1)    
        return res

        # return the median    
        # return sorted(nums)[len(nums)//2]
