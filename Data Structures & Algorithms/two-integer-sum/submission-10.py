class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = set()
        for i, chari in enumerate(nums):
            hashset.add(chari)
            if chari in hashset:
                for j, charj in enumerate(nums):
                    if i != j and chari + charj == target:
                        idx = sorted([i, j])
                        return idx
            for j, charj in enumerate(nums):
                if i != j and chari + charj == target:
                    idx = sorted([i, j])
                    return idx