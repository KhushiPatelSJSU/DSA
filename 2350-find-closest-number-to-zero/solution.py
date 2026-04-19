class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]

        for i in nums:
            if abs(i) < abs(closest):
                closest = i
            elif abs(i) == abs(closest):
                closest = max(i, closest)
        return closest
