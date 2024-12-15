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