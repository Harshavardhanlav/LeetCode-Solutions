class Solution(object):
    def longestCommonPrefix(self, strs):
        commonString = strs[0]

        for i in range(1, len(strs)):
            current = strs[i]

            j = 0

            while j < min(len(commonString), len(current)):
                if commonString[j] != current[j]:
                    break
                j += 1

            commonString = commonString[:j]

            if commonString == "":
                return ""

        return commonString