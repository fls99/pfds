def betrayers_badge(list_num: list[int], badge_num: int) -> list[int]:
    if 0 <= badge_num < len(list_num):
        list_num.pop(badge_num)
    return [i for i in list_num if i != badge_num]



ancient_scroll = list(map(int, input().split()))
badge = int(input())
output = betrayers_badge(ancient_scroll, badge)
print(output)