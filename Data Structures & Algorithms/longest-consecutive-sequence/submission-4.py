class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(bool)
        for num in nums:
            mp[num] = True
        
        ans = 0
        curr_max = 1

        for num in nums:
            if num-1 in mp:
                continue
            else:
                length = 1
                while (num + length) in mp:
                    length+=1
                ans = max(length, ans)
        
        return ans