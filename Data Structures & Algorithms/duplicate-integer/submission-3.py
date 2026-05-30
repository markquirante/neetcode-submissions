class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # brute force is to store each new element in a list, if seen before return true

        seen_number = set()

        for num in nums:
            if num in seen_number:
                return True
            
            seen_number.add(num)
        
        return False