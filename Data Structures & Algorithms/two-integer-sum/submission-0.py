class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            new_target = target - num

            if new_target in hashmap:
                return [hashmap[new_target], i]

            hashmap[num] = i