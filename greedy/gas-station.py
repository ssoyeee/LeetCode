class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, tank, start = 0, 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if tank < 0:
                start = i +1
                tank = 0
        return start if total >=0 else -1

        #T: O(N) -- where N is len(gas)
        #S: O(1) -- three variables
