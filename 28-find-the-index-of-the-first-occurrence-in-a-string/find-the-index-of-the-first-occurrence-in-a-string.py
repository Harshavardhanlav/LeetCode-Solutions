class Solution(object):
    def strStr(self, haystack, needle):
        i = 0
        j = len(needle)
        while j <= len(haystack):
            res = haystack[i:j]
            if res == needle:
                return i
            i+=1
            j+=1
        return -1