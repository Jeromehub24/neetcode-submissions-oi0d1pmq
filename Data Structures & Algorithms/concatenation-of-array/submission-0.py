class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #Create an array ans of length 2n
        #ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
        two_nums = nums + nums
        return two_nums