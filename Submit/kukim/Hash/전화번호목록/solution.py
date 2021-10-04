"""
	문제    : 전화번호목록
    유형    : 해쉬, set
	난이도  : 중 lv2
	시간    : 15m
	uri    : https://programmers.co.kr/learn/courses/30/lessons/42577
"""
#### case 1 : list
def solution(phoneBook):
    phoneBook.sort()
    for prev, next in zip(phoneBook[:-1], phoneBook[1:]):
        if next.startswith(prev):
            return False
    return True

#### case 2 : hash & set
def solution(phoneBook):
    hash_map = set()
    
    for phone_number in phoneBook:
        hash_map.add(phone_number)
    
    for phone_number in phoneBook:
        string = ""
        for number in phone_number:
            string += number
            if string in hash_map and string != phone_number:
                return False
    return True