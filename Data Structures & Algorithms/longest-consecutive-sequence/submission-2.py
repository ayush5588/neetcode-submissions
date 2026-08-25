class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n == 0 or n == 1:
            return n
        
        ans = 1
        curr_max = 1
        for i in range(n-1):
            if nums[i] == (nums[i+1]-1):
                curr_max += 1
                ans = max(ans, curr_max)
            elif nums[i] == nums[i+1]:
                continue
            else:
                curr_max = 1
        
        ans = max(ans,curr_max)
        return ans

