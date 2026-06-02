class Solution(object):
    def minCostClimbingStairs(self, cost):

        dp1 = cost[0]
        dp2 = cost[1]

        for i in range(2, len(cost)):
            current = cost[i] + min(dp1, dp2)

            dp1 = dp2
            dp2 = current

        return min(dp1, dp2)