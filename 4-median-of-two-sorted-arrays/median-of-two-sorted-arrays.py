class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1+nums2
        nums3.sort()
        if len(nums3) % 2 != 0:
            return float(nums3[int(len(nums3)/2)])
        else:
            i = int(len(nums3)/2)
            j = i-1
            if nums3[i] == nums3[j]:
                return nums3[j]
            return (nums3[i]+nums3[j])/2