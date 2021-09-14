from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        ans = []
        cnt_nums = Counter(nums)
        count = 0
        for elem in sorted(cnt_nums.items(), key=lambda x: x[1], reverse=True):
            if count < k:
                ans.append(elem[0])
                count += 1
            else:
                break

        return ans
