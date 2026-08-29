class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, count = 0, 0
        for n in nums:
            if n == 1:
                count += 1
                print(count)
            else:
                count = 0
            res = max(res, count)
        return res