class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [h : i]
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                stackH, stackI = stack.pop()
                maxArea = max(maxArea, (i - stackI) * stackH)
                start = stackI
            stack.append([h, start])
        for h, i in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea