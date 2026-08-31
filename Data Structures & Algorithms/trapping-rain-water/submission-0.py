class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_arr = [0]*n
        suffix_arr = [0]*n

        prefix_arr[0] = height[0]
        for i in range(1,n):
            prefix_arr[i] = max(prefix_arr[i-1],height[i])
        
        suffix_arr[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            suffix_arr[i] = max(suffix_arr[i+1], height[i])
        
        cnt = 0
        for i in range(n):
            cnt += min(prefix_arr[i], suffix_arr[i]) - height[i]
        
        return cnt