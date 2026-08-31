class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        i = 0
        while i < n-2:
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue
            j, k = i+1, n-1
            while j < k:
                add = nums[i] + nums[j] + nums[k]
                if add == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif add > 0:
                    k -= 1
                else:
                    j += 1
        
            i+=1
        
        return ans
