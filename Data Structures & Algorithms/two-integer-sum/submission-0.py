class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for index, value in enumerate(nums):
            diff = target - value

            if diff in freq:
                return [freq[diff], index]
        
            freq[value] = index      