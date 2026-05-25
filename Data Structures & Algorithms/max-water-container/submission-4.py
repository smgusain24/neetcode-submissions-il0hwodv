class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n-1
        maxVol = 0
        while left<right:
            vol = min(heights[left],heights[right]) * (right-left)
            maxVol = max(maxVol, vol)
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
        return maxVol
