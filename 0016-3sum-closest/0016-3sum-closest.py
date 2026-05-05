class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)

        closest = float('inf')

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                curr_sum = nums[i] + nums[left] + nums[right]

                # update closest
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                # move pointers
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum  # exact match

        return closest