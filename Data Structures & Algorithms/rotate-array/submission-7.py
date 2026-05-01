from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        count = 0
        start = 0

        while count < n:
            curr = start
            prev = nums[start]

            while True:
                nxt = (curr + k) % n
                nums[nxt], prev = prev, nums[nxt]
                curr = nxt
                count += 1

                if curr == start:
                    break

            start += 1