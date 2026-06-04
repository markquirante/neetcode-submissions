class Solution:

    def encode(self, strs: List[str]) -> str:
        
        result = []

        for s in strs:
            result.append(str(len(s)) + "#" + s)

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            word_len = int(s[i:j])

            start = j + 1
            end = start + word_len

            result.append(s[start:end])

            i = end

        return result
