class Solution:

    def __init__(self):
        pass

    def numMatchingSubseq(self, S: str, words: list[str]) -> int:
        a = 0

        for b in words:
            c = 0
            for i in range(len(b)):
                d = S[c:].find(b[i])
                if d < 0:
                    a -= 1
                    break
                else:
                    c += d + 1
            a += 1

        return a
