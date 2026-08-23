class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr_s = [1]*n
        arr_p = [1]*n

        # prefix array prep
        for i in range(1,n):
            arr_p[i] = arr_p[i-1] * nums[i-1]

        # suffix array prep
        for i in range(n-2,-1,-1):
            arr_s[i] = arr_s[i+1] * nums[i+1]
        
        arr = [1]*n
        for i in range(n):
            arr[i] = arr_p[i] * arr_s[i]
        
        return arr