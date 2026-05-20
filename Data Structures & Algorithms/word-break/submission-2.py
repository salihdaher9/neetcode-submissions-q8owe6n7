class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)

        memo = {}

        def dfs(l, r):
            # If l reached the end, we successfully split all string
            if l == n:
                return True

            # If r reached the end but l did not, no more word to try
            if r == n:
                return False

            if (l, r) in memo:
                return memo[(l, r)]

            curr = s[l:r+1]

            # Option 1: if current substring is a word, take it
            take = False
            if curr in words:
                take = dfs(r + 1, r + 1)

            # Option 2: do not take it yet, expand r
            skip = dfs(l, r + 1)

            memo[(l, r)] = take or skip
            return memo[(l, r)]

        return dfs(0, 0)