class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        
        subset = []
        def dfs(i): #index [0, 1, 2] of the values [1, 2, 3]
            if i >= len(nums): #out of bounds
                out.append(subset.copy()) 
                return
            
            #decision to include nums[i] -> left side  1, 2, 3
            subset.append(nums[i])
            dfs(i+1)

            #decision NOT to include nums[i] -> right side []
            subset.pop()
            dfs(i+1)
        
        dfs(0) #start backtracking from the beginning
        return out