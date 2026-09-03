class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree: no cycles, all connected
        if not n:
            return True
        adj = { i:[] for i in range(n) }
        for p, c in edges:
            adj[p].append(c)
            adj[c].append(p)
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        return dfs(0, -1) and n == len(visit)