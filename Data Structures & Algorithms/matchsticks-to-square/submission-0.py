class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total // 4
        sides = [0, 0, 0, 0]

        matchsticks.sort(reverse=True)

        def backtrack(index):
            if index == len(matchsticks):
                return (
                    sides[0] == target and
                    sides[1] == target and
                    sides[2] == target and
                    sides[3] == target
                )

            stick = matchsticks[index]

            for i in range(4):
                if sides[i] + stick <= target:
                    sides[i] += stick

                    if backtrack(index + 1):
                        return True

                    sides[i] -= stick

            return False

        return backtrack(0)