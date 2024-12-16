'''
746. Min Cost Climbing Stairs | Easy
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 
Constraints:
2 <= cost.length <= 1000
0 <= cost[i] <= 999
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Recursive
        # T: O(2^n)
        # S: O(n)
        n = len(cost)

        def min_cost(i): #helper func
            if i < 2:
                return 0
            return min(cost[i-2] + min_cost(i-2), cost[i-1] + min_cost(i-1))

        return min_cost(n)
        
        
        # Top Down DP (Memoization)
        # T: O(2^n)
        # S: O(n)
        '''
        n = len(cost)
        memo = {0:0, 1:0}
        def min_cost(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = min(cost[i-2] + min_cost(i-2), cost[i-1] + min_cost(i-1))
                return memo[i]
        
        return min_cost(n)
        '''
        # Bottom Up DP (Tabulation)
        # T: O(n)
        # S: O(n)
        '''
        n = len(cost)
        dp = [0] * (n+1)
        
        for i in range(2, n+1):
            dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        return dp[n]
        '''
        # Bottom Up DP (Two Pointers, Constant Space) 
        # T: O(n)
        # S: O(1)
        '''
        n = len(cost)
        prev, curr = 0, 0

        for i in range(2, n+1):
            prev, curr = curr, min(cost[i-2] + prev, cost[i-1]+curr)
        return curr
        '''