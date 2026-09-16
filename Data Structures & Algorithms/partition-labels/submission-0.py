class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size, end = 0, 0
        last = {}

        for i, c in enumerate(s):
            last[c] = i
        res = []
        for i, c in enumerate(s):
            size += 1
            end = max(end, last[c])
            if i == end:
                res.append(size)
                size = 0
        return res