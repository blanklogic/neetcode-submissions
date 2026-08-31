class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms

        # if len(nums) == 0:
        #             return [[]]
        # perms = self.permute(nums[1:]) # O(n!)
        # res = []
        # for p in perms: # O(n)
        #     for i in range(len(p) + 1):
        #         p_copy = p.copy()
        #         p_copy.insert(i, nums[0]) # O(n)
        #         res.append(p_copy)

        # return res