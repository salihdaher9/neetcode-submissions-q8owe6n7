class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(target, candidates, curr):
            if target == 0:
                res.append(curr[:])
                return
            if target < 0 or not candidates:
                return

            first = candidates[0]

            # Include
            curr.append(first)
            dfs(target - first, candidates[1:], curr)
            curr.pop()

            # Exclude (skip duplicates)
            i = 1
            while i < len(candidates) and candidates[i] == first:
                i += 1

            dfs(target, candidates[i:], curr)

        dfs(target, candidates, [])
        return res