class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(numbers):
            needed = target - num
            if needed in seen:
                return [seen[needed], i + 1]
            else:
                seen[num] = i + 1
