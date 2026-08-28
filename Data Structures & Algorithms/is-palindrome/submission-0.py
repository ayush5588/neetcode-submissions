class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        w = [c for c in s if c.isalnum()]
        withoutAlnum = "".join(w)
        arr = withoutAlnum.strip()
        cleaned = "".join(arr)

        sent = cleaned.lower()

        i, j = 0, len(sent)-1
        while i < j:
            if sent[i] == sent[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True