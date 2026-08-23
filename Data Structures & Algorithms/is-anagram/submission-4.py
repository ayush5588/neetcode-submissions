class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        arr = [0]*26
        for i in range(len(s)):
            s_idx = ord(s[i]) - ord('a')
            t_idx = ord(t[i]) - ord('a')
            arr[s_idx] += 1
            arr[t_idx] -= 1

        for i in range(len(arr)):
            if arr[i] != 0:
                return False
        
        return True