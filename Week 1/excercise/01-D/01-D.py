def betrayers_badge(list_num: list[int], badge_num: int) -> list[int]:
    list_num.pop()
    list_num.pop(badge_num)
    return [i for i in list_num if i != badge_num]



x: list[int] = list(map(int, input().split()))
output = betrayers_badge(x, x[-1])
print(output)