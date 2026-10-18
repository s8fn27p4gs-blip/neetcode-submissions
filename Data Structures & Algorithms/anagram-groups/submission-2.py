class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        seen = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in seen:
                seen[sorted_word] = []

            seen[sorted_word].append(word)

        return list(seen.values())