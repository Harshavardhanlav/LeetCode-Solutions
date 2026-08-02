class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max2 = 0
        total = 0
        for i in range (0, len(nums)):
            if nums[i] == 1:
                total = total + 1
            else:
                if max2 < total:
                    max2 = total
                total = 0
            if i == len(nums)-1 :
                if max2 < total:
                    max2 = total
        return max2
        