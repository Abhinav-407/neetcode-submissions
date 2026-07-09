class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        bucket = [[] for _ in range(len(nums)+1)]
        out = []
        for key,value in freq.items():
            bucket[value].append(key)
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                out.append(num)
                if len(out) == k:
                    return out
        
