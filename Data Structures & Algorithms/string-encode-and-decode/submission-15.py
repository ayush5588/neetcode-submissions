class Solution:

    def encode(self, strs: List[str]) -> str:
        self.pattern = "#!"
        encoded_str = ""
        for s in strs:
            encoded_str += self.pattern + s
        encoded_str += self.pattern
        return encoded_str
    def decode(self, s: str) -> List[str]:
        arr = s.split(self.pattern)
        return arr[1:len(arr)-1]