class Solution(object):
    def sortColors(self, arr):
        i = 0
        j = 0
        k = len(arr)-1
        while j<=k:
            if arr[j] == 0:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i+=1
                j+=1
            elif arr[j] == 1:
                j+=1
            elif arr[j] == 2:
                arr[j],arr[k] = arr[k],arr[j]
                k-=1