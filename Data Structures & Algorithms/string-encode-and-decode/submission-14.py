class Solution:
    def encode(self, strs: List[str]) -> str:
        self.pattern = ".#$."
        encoded_str = ""
        for s in strs:
            encoded_str += self.pattern + s
        encoded_str += self.pattern
        return encoded_str

    def decode(self, s: str) -> List[str]:
        ans = s.split(self.pattern)
        return ans[1:len(ans)-1]
