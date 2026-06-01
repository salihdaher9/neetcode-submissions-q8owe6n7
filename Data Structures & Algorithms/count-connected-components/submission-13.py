class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return

            # attach smaller-rank tree under bigger-rank tree
            if rank[rootA] > rank[rootB]:
                parent[rootB] = rootA

            elif rank[rootA] < rank[rootB]:
                parent[rootA] = rootB

            else:
                parent[rootB] = rootA
                rank[rootA] += 1

        for a, b in edges:
            union(a, b)

        components = set()

        for i in range(n):
            components.add(find(i))

        return len(components)