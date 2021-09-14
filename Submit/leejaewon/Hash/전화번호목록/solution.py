from collections import deque

def solution(phone_book):
    ## 목표: phone_book의 원소중에 다른 원소의 접두어인 경우가 있으면 False, 아니면 True 리턴
    ## 1. phone_book을 사전 순으로 정렬
    ## 2. phone_book을 deque로 재할당
    ## 3. phone_book에서 원소 한개씩 추출하여 prefix로 할당
    ## 4. prefix가 phone_book의 첫번째 원소의 접두어 라면 return False
    ## 5. 1번부터 4번까지 반복
    ## 6. 반복문이 끝나면 return True
    
    phone_book.sort()
    
    for p, s in zip(phone_book, phone_book[1:]):
        if s.startswith(p):
            return False
    else:
        return True
#     phone_book = deque(phone_book)
    
#     while phone_book:
#         prefix = phone_book.popleft()
        
#         if phone_book and all(map(lambda x: x[0] == x[1], zip(prefix, phone_book[0]))):
#             return False

#     return True