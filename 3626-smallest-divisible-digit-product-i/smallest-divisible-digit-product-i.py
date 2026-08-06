class Solution(object):
    def smallestNumber(self, n, t):
        found = False
        while found == False:
            q = n
            mul= 1
            while q > 0:
                mul = mul * (q%10)
                q = q//10
            if mul % t == 0:
                found = True
                return n
            else:
                n=n+1
