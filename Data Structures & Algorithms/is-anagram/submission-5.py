class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # first check if the both strings are the same length
        if len(s) != len(t):
            return False
        
        s_hash = {}
        for char in s:
            s_hash[char] = s_hash.get(char, 0) + 1

        t_hash = {}
        for char in t:
            t_hash[char] = t_hash.get(char, 0) + 1
        
        print(f"this is s_hash: {s_hash}")

        print(f"this is t_hash: {t_hash}")

        if s_hash == t_hash:
            return True
        
        return False


