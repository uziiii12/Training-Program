class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj=[]
        for i in range(n):
            adj.append([])
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = {source}
        queue = [source]
        while queue:
            curr = queue.pop(0)
            if curr == destination:
                return True
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False