class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        maxi_num = nums[0]
        for val in nums[1:]:
            curr = max(val, val + curr)
            maxi_num = max(maxi_num, curr)
        return maxi_num
        