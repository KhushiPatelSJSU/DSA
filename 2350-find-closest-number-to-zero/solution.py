class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]

        for val in nums:
            if abs(val) < abs(closest):
                closest = val

        if (closest < 0 and abs(closest) in nums):
            return abs(closest)
        else:
            return closest
