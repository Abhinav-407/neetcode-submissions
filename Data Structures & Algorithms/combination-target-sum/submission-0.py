class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        result = []

        def backtrack(start, current_sum):
            if current_sum == target:
                result.append(path.copy())
                return
            if current_sum > target:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, nums[i] + current_sum)
                path.pop()

        backtrack(0,0)
        return result