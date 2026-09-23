class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d_t={}
        for i in range(0,len(t)):
            if t[i] in d_t:
                f=d_t[t[i]]
                d_t[t[i]]=f+1
            else:
                d_t[t[i]]=1
        for i in range(0,len(s)):
            f=d_t[s[i]]
            d_t[s[i]]=f-1
        for i in d_t.keys():
            if d_t[i]==1:
                return i       