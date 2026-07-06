class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurrences = Counter(nums)
        print(occurrences)

        most_common = occurrences.most_common(1)
        return most_common[0][0]