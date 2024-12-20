/*
70. Climbing Stairs|Easy

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:
1 <= n <= 45

*/

class Solution {
    private static int memo[];
    public static int recur(int n){
        // initial condition
        if (n==1){
            return 1;
        }
        if (n==2){
            return 2;
        }
        if (memo[n]  != 0){
            return memo[n];
        }
        // recurrence relation
        return memo[n] = recur(n-1)+recur(n-2);
    }

    public int climbStairs(int n) {
        memo = new int[n+1];
        return recur(n);
    }
}
// c[n] = number of cases for climbing n stairs
// c[n] = c[n-1]+c[n-2]