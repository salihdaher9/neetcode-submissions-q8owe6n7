class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res=[]

        subset=[]
        def dfs():
            if sum(subset)==target:
                res.append(subset[:])
                return
            if sum(subset)>target:
                return
            
            for i in nums:
                if subset:
                    if i>=subset[-1]:
                        subset.append(i)
                        dfs()
                        subset.pop()
                else:
                    subset.append(i)
                    dfs()
                    subset.pop()
        dfs()
        return res