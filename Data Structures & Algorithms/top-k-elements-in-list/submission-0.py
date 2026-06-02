class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # I want to keep a frequency of each number
        freq_list = {}

        for num in nums:
            freq_list[num] = freq_list.get(num, 0) + 1

        print(freq_list)
        
        # get the highest key value in freq_list
        highest = max(freq_list.values())
        
        # iterate through dict up to 'k' value
        result = []

        while len(result) < k:
            for key, value in freq_list.items():
                if value == highest:
                    result.append(key)

                    if len(result) == k:
                        return result
            
            highest -= 1
        
        return result
