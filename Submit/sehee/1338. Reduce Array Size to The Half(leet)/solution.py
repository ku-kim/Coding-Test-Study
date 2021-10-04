from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        count = Counter(arr).most_common()

        sum = 0
        for i, c in enumerate(count):
            sum += c[1]
            if sum >= len(arr) // 2:
                return i + 1
