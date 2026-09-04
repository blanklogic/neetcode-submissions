class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MST
        n = len(points)
        adj = { i:[] for i in range(n) }
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # Prim's
        res = 0
        visit = set()
        frontier = [[0, 0]] # (w, n)
        while len(visit) < n:
            w, i = heapq.heappop(frontier)
            if i in visit:
                continue
            res += w
            visit.add(i)
            for neiW, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(frontier, [neiW, nei])
        return res