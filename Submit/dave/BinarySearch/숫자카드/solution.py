# With Hash
N = int(input())
cards = dict()
for card_num in map(int, input().split()):
    cards[card_num] = card_num
res = list()
M = int(input())
for num in map(int, input().split()):
    try:
        if cards[num]:
            res.append(1)
    except KeyError:
        res.append(0)

print(' '.join(map(str, res)))


# With Binary Search
N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())

res = list()
for num in map(int, input().split()):
    s = 0
    e = N - 1
    is_hit = False
    while s <= e:
        m = s + (e - s) // 2
        if cards[m] == num:
            res.append(1)
            is_hit = True
            break
        elif cards[m] > num:
            # find on left side
            e = m - 1
        else:
            # find on right side
            s = m + 1
    if not is_hit:
        res.append(0)

print(' '.join(map(str, res)))

