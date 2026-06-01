class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent=[i for i in range(n)]


        def find(x):
            if parent[x]!=x:
                return find(parent[x])
            return x


        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA != rootB:
                parent[rootB] = rootA
        
        
        for i,j in edges:
            union(i,j)
        s=set()
        for i in parent:
            if not find(i) in s:
                s.add(find(i))
        print(parent)
        return len(s)
