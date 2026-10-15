class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenHash = set()

        for n in nums:
            if n in seenHash:
                return True
            
            seenHash.add(n)

        return False