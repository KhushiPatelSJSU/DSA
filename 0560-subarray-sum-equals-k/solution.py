class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix_sum = {0: 1}

        for num in nums:
            curr_sum += num
            needed = curr_sum - k

            if needed in prefix_sum:
                count += prefix_sum[needed]

            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
        
        return count
