class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i, num in enumerate(nums):
            if target - nums[i] in checked:
                return[checked[target - num], i]
            else:
                checked[num] = i