class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mp = {}

        for i in range(n):
            mp[nums[i]] = i


        for i in range(n):
            b = target - nums[i]
            if b in mp and mp[b] != i:
                if i > mp[b]:
                    return [mp[b],i]
                else:
                    return [i, mp[b]]