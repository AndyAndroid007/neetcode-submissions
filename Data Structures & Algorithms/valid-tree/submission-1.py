class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj_list = {i:[] for i in range(n)}

        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def dfs(node,par):
            visited.add(node)
            for nei in adj_list[node]:
                if nei in visited:
                    if nei == par:
                        continue
                    return False
                if not dfs(nei,node):
                    return False
            return True

        return dfs(0,-1) and len(visited) == n
        
        