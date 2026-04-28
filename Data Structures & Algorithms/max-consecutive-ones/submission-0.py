class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        beat = 0
        for i in nums:
            if i == 1:
                current += 1
            if i == 0:
                current = 0
            if current> beat:
                beat = current


        return beat
        