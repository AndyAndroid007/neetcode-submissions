class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        N = len(words)
        seen = set()
        for i in words:
            for j in i:
                seen.add(j)
        K = len(seen)
        print(K)
        adj = {i: [] for i in seen}


        def adj_builder(a,b):
            
            m,n = len(a), len(b)
            if n < m and a[:n] == b:
                return False
            
            for i in range(min(m,n)):
                if a[i] != b[i]:
                    adj[a[i]].append(b[i])
                    break
            return True

        for i in range(N-1):
            if not adj_builder(words[i],words[i+1]):
                return ""

        final = []
        state = {c:0 for c in seen}
        def dfs(node):
            state[node] = 1
            for neighbor in adj[node]:
                if state[neighbor] == 1:
                    return False
                if state[neighbor] == 0:
                    if not dfs(neighbor):
                        return False
            state[node] = 2
            final.append(node)
            return True

        for c in seen:
            if state[c] == 0:
                if not dfs(c):
                    return ""

        return "".join(final[::-1])
        