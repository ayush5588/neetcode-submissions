class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, a in enumerate(nums):
            b = target - a
            if b in seen:
                return [seen[b], idx]
            seen[a] = idx