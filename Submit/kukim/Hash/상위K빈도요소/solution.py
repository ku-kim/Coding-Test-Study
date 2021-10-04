from typing import List
import collections

# case 1 : kukim, pythonic
def topKFrequent(nums: List[int], k: int) -> List[int]:
    counts = collections.Counter(nums).most_common(k)
    result = []
    for key in counts:
        result.append(key[0])
    return result

# case 2 : 기본 dict kukim
def topKFrequent(nums: List[int], k: int) -> List[int]:
    counts = {}
    result = []
    for i in nums:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
    res = sorted(counts.items(), key = lambda x: x[1], reverse=True)
    for i in range(k):
        result.append(res[i][0])
    return result

# case 3 : defaultdict kukim
def topKFrequent(nums: List[int], k: int) -> List[int]:
    counts = collections.defaultdict(int)
    result = []
    for i in nums:
        counts[i] += 1
    res = sorted(counts.items(), key = lambda x: x[1], reverse=True)
    for i in range(k):
        result.append(res[i][0])
    return result


# case 2 : 간결한 pythonic
def topKFrequent(nums: List[int], k: int) -> List[int]:
    return list(zip(*collections.Counter(nums).most_common(k)))[0]

nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums,k))