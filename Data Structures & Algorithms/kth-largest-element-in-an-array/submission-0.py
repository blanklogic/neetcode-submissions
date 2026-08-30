class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
        
        # heapq.heapify_max(nums)
        # while k > 0:
        #     res = heapq.heappop_max(nums)
        #     k -= 1
        # return res

        # nums = [-n for n in nums]
        # heapq.heapify(nums)
        # while k > 0:
        #     res = heapq.heappop(nums)
        #     k -= 1
        # return abs(res)