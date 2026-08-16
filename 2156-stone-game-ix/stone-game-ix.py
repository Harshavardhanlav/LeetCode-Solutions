class Solution(object):
    def stoneGameIX(self, stones):
        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        zero = count[0]
        one = count[1]
        two = count[2]

        if one == 0 and two == 0:
            return False

        if zero % 2 == 0:
            return one > 0 and two > 0

        return abs(one - two) > 2