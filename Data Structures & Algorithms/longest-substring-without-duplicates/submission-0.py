class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, 0
        st = set()
        max_len = 0
        while r < n:
            if s[r] not in st:
                st.add(s[r])
                max_len = max(max_len, (r-l)+1)
                r += 1
            else:
                while s[r] in st:
                    st.discard(s[l])
                    l+=1
        
        return max_len