class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i in range(0,len(nums)):
            if nums[i] != 0 :
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j+=1
        