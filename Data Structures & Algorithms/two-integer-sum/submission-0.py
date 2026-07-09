class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, num in enumerate(nums):
            comp = target - num
            if num in check:
                return [check.get(num), i]
            check[comp] = i