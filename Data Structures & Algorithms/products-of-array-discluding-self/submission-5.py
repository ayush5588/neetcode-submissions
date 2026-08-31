class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = 1
        zero_cnt = 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                product *= num
        
        if zero_cnt > 1:
            return [0]*n

        ans = []
        for num in nums:
            if num != 0:
                if zero_cnt > 0:
                    ans.append(0)
                else:
                    ans.append(product//num)
            else:
                ans.append(product)
        
        return ans