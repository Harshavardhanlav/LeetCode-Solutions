class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        max_sum = sum(cardPoints[0:k])
        win = max_sum
        n =len(cardPoints)-1
        for i in range(k):
            win = win - cardPoints[k-i-1] + cardPoints[n-i]
            max_sum = max(win , max_sum)
        return max_sum