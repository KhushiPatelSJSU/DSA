class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen1 = set(nums1)
        result = set()

        for x in nums2:
            if x in seen1:
                result.add(x)

        return list(result)

