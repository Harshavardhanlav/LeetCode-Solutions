class Solution(object):
    def maximumLengthSubstring(self, arr):
        maxLen = 0;
        subString = ""
        l = 0;
        for r in range(0,len(arr)):
            check = False
            subString+=arr[r]
            for s in subString:
                if subString.count(s) > 2:
                    l+=1;
                    subString = subString[1:]
                    check = True
                    break
            if check == False:
                maxLen = max(maxLen, len(subString))
        return maxLen

        