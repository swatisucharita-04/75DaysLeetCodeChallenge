class Solution(object):
    def findDisappearedNumbers(self, nums):
        
        n = len(nums)
        s = set(nums)
        result = []

        for i in range(1, n+1):
            if i not in s:
                result.append(i)

        return result