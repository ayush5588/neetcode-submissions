class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq_arr = [[] for i in range(n+1)]

        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for num, freq in count.items():
            freq_arr[freq].append(num)
        
        ans = []
        for i in range(len(freq_arr)-1,-1,-1):
            arr = freq_arr[i]
            arr_len = len(arr)-1
            while k > 0 and arr_len >= 0:
                ans.append(arr[arr_len])
                arr_len -= 1
                k -= 1
        
        return ans