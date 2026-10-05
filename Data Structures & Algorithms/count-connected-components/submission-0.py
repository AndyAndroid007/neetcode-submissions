class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i:[] for i in range(n)}
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()

        def dfs(node):
            visited.add(node)

            for nei in adj_list[node]:
                if nei not in visited:
                    dfs(nei)
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
        