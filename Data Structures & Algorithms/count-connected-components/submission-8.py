class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = {}

        c = [set() for i in range(n)]

        for i, j in edges:
            if not i in d and not j in d:
                d[i] = i
                d[j] = i
                c[i].add(i)
                c[i].add(j)

            elif i in d and not j in d:
                place = d[i]
                c[place].add(j)
                d[j] = place
            
            elif j in d and not i in d:
                place = d[j]
                c[place].add(i)
                d[i] = place
            elif i in d and j in d:
                place_i = d[i]
                place_j = d[j]

                if place_i != place_j:
                    # move all nodes from place_j into place_i
                    for node in c[place_j]:
                        c[place_i].add(node)
                        d[node] = place_i

                    # empty old component
                    c[place_j].clear()

        res = 0
        print(c)

        for s in c:
            if s:
                res += 1

        # count isolated nodes
        for i in range(n):
            if i not in d:
                res += 1

        return res