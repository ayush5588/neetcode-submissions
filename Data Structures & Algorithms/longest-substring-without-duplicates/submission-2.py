class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, 0
        mp = defaultdict(int)
        max_len = 0
        while r < n:
            while s[r] in mp:
                l = max(mp[s[r]]+1, l)
                del mp[s[r]]
            mp[s[r]] = r
            max_len = max(max_len, r - l + 1)
            r += 1
        

        return max_len

