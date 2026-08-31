class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        n = len(st)
        if n == 0 or n == 1:
            return n
        ans = 1
        for num in st:
            if num-1 in st:
                continue
            cnt = 1
            while num+cnt in st:
                cnt += 1
            ans = max(ans, cnt)
            cnt = 1
        return ans