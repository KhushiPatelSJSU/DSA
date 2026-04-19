class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, x in enumerate(nums):
            if x in seen and (abs(seen[x] - i) <= k):
                return True
            seen[x] = i
        return False