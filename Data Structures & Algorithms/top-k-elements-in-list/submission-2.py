class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}

        for i in nums:
            c[i] = c.get(i, 0) + 1

        res = [[] for _ in range(len(nums) + 1)]

        for i in c:
            res[c[i]].append(i)

        ress = []

        for i in range(len(nums), -1, -1):
            for x in res[i]:
                ress.append(x)

                if len(ress) == k:
                    return ress