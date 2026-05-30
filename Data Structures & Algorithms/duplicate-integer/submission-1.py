class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # brute force way is to check each element as they are added to a new list

        # since we are checking duplicates I am using a list instead of a set() for look up
        seen_nums = []

        # check if list is infinite then just return false
        if len(nums) > sys.maxsize:
            return False

        for num in nums:
            if num in seen_nums:
                return True
            
            seen_nums.append(num)
        
        # if there are no duplicates
        return False
