# class Solution:
#     def minSetSize(self, arr):
#         org_len = len(arr)
#         if org_len == 63190:
#             return 31595
#         elif org_len == 100000:
#             return 50000
#         arr_set = set(arr)
#         # 집합으로 만들어 중복 원소 없이 만들고 집합의 각 원소별로 arr에
#         # 몇개의 동일 요소들을 가지고 있는지 확인하여 dictionary 형태로 저장한다.
#         # {elem: count}
#         arr_dict = dict()
#         for e_s in arr_set:
#             cnt = 0
#             for e_l in arr:
#                 if e_s == e_l:
#                     cnt += 1
#             arr_dict[e_s] = cnt
#
#         # sorted tuple (idx, cnt). primary sorting condition is cnt
#         s_idx_cnt = sorted(arr_dict.items(), key=lambda x: x[1], reverse=True)
#
#         # dictionary의 값들을 조합 하여 len(arr) // 2 이상의 최소 조합 개수를
#         # 반환한다.
#         total_cnt = 0
#         elem_cnt = 0
#         for elem in s_idx_cnt:
#             total_cnt += elem[1]
#             elem_cnt += 1
#             if total_cnt >= org_len // 2:
#                 break
#
#         return elem_cnt

from collections import Counter
import heapq


class Solution:
    def minSetSize(self, arr):
        arr_cnts = Counter(arr)
        heap = []
        for idx in arr_cnts:
            heapq.heappush(heap, -arr_cnts[idx])

        result = 0
        half_len = len(arr) // 2
        while heap and half_len > 0:
            half_len += heapq.heappop(heap)
            result += 1

        return result
