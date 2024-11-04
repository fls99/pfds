
def split_list(a_list:list[int]):
    """
    Splits a given even list in half

    @a_list: An list with even length
    @return two lists splitted in half

    """
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def rune_rumble(runes:list) -> int:
    """
    Compares the rune in a 1:1 battle for each clan and returns the total power of all matches won
    
    @runes: A list containing the power of each clan
    @return: Returns the winner of the battle indicated as the maximum power of all won battles
    """
    runes_griffon, runes_phoenix = split_list(runes)

    counter_griffon: int = 0
    counter_phoenix: int = 0

    for i in range(len(runes_griffon)):
        if runes_griffon[i] > runes_phoenix[i]:
            counter_griffon += runes_griffon[i]
        else:
            counter_phoenix += runes_phoenix[i]
    
    return max(counter_phoenix, counter_griffon)

runes = list(map(int, input().split()))
x = rune_rumble(runes)
print(x)




