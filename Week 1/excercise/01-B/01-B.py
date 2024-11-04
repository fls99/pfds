# number of coins not divisivle by 2 or 3 

def coin_condrum(limit: int) -> int:
    current_sum = 0
    for i in range(limit):
        if i % 2 != 0 and i % 3 != 0:
            if current_sum + i >= limit:
                break
            current_sum += i
    return current_sum

x = coin_condrum(7588)
print(x)