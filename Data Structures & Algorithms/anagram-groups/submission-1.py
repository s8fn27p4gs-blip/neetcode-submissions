class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        seen = {} #create buckets

        for word in strs:
            sorted_word = "".join(sorted(word)) #so we know how to group
            if sorted_word not in seen:
                seen[sorted_word] = [] #create new bucket

            seen[sorted_word].append(word)
            
        return list(seen.values())