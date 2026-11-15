class Solution:

    def encode(self, strs: List[str]) -> str:
        start = "<start>"
        end = "<end>"
        delimiter = "||"

        n = len(strs)
        if (n == 0):
            return "<empty>"
        # test = []
        # print(f"len of test: {len(test)}")
        # encoded = [0] * (n + n-1 + 2)

        # encoded[0] = start
        # encoded[2*n] = end

        encoded = delimiter.join(strs)
        encoded = start + encoded + end

        return encoded




    def decode(self, s: str) -> List[str]:

        if s == "<empty>":
            return []
        s = s[7:-5]
        input = s.split("||")
        return input






