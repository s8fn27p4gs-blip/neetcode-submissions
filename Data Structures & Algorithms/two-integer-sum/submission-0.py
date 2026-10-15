class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0

        for n in nums:
            diff = target - n

            if diff in seen:
                return [seen[diff], i]
            
            seen[n] = i
            i += 1
        return []