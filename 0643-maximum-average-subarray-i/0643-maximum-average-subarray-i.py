class Solution(object):
    def findMaxAverage(self, nums, k):

        # first window sum
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # slide window
        for i in range(k, len(nums)):
            window_sum += nums[i]      # add new
            window_sum -= nums[i-k]    # remove old

            max_sum = max(max_sum, window_sum)

        return float(max_sum) / k