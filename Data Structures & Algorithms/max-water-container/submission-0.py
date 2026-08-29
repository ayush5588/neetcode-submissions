class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1
        ans = 0
        while l < r:
            vol = min(heights[l], heights[r]) * (r-l)
            ans = max(ans, vol)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return ans