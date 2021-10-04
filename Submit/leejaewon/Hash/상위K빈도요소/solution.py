def topKFrequent(nums, k):
        ## 목표: 가장 많이 등장하는 상위 K가지 요소를 뽑아서 리턴
        ## 1. Counter로 원소가 각각 몇개인지 딕셔너리 생성
        ## 2. Counter 딕셔너리를 키값 순으로 정렬
        ## 3. K번째 원소까지 키를 출력
        
        num_count = Counter(nums)
        num_count = dict(sorted(num_count.items(), key=lambda x: x[1], reverse=True))
        
        return list(num_count.keys())[:k]