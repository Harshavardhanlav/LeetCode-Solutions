class Solution(object):
    def smallestIndex(self, nums):
        for i in range(0,len(nums)):
            digit = nums[i]
            sum = 0;
            while digit>0:
                rem = digit %10;
                sum = sum+rem;
                digit = digit//10
            if sum == i:
                return i
        return -1
    