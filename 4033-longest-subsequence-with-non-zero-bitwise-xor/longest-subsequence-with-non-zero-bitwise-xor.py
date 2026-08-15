class Solution(object):
    def longestSubsequence(self, nums):
        x=0
        latestValue = nums[len(nums)-1]
        result = all(v == 0 for v in nums)
        if result: return 0
        for i in range(0, len(nums)):
            x^=nums[i]
        print(x)
        if x != 0:
            return len(nums)
        return len(nums)-1