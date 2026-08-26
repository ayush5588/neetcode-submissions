class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        
        ans = 0
        curr_max = 1

        for num in numbers:
            if num-1 in numbers:
                continue
            else:
                length = 1
                while (num + length) in numbers:
                    length+=1
                ans = max(length, ans)
        
        return ans