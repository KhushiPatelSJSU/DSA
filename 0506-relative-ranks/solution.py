class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        ranks = {}    # For O(n) complexity, we use map instead of sorted_scores.index(s)

        for i, s in enumerate(sorted_scores):
            if i == 0:
                ranks[s] = "Gold Medal"
            elif i == 1:
                ranks[s] = "Silver Medal"
            elif i == 2:
                ranks[s] = "Bronze Medal"
            else:
                ranks[s] = str(i + 1)

        return [ranks[s] for s in score]
