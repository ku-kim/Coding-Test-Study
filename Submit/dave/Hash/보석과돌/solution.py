from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        stones_cnt = Counter(stones)
        for jewel in jewels:
            ans += stones_cnt[jewel]
        return ans
