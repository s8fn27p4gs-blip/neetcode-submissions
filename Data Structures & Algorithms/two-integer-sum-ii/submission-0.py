class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers)-1

        while index1 < index2:
            current_sum = numbers[index1] + numbers[index2]
            
            # Bug 3 Fixed: Handle the perfect match condition first
            if current_sum == target:
                return [index1 + 1, index2 + 1] # 1-based index 

            if numbers[index1] + numbers[index2] < target:
                index1 += 1

            else:
                index2 -= 1   

        return []        