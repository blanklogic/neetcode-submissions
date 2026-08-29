class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow] # 1, 2
            fast = nums[nums[fast]] # 2, 2
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow] # 3, 2
            slow2 = nums[slow2] # 1, 2
            if slow == slow2:
                return slow