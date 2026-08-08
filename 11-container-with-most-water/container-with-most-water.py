class Solution(object):
    def maxArea(self, arr):
        left = 0
        right = len(arr)-1
        maxEle = 0
        distance = len(arr)-1
        while left <= right:
            if arr[left] >= arr[right]:
                res = arr[right] * distance;
                if maxEle < res:
                    maxEle = res
                distance-=1
                right-=1
            elif arr[left] < arr[right]:
                res = arr[left] * distance
                if maxEle < res:
                    maxEle = res
                distance-=1;
                left+=1
        return maxEle
        