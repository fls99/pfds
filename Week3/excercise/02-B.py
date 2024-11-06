odd_seq = [int(i) for i in input().split(sep=" ") if i%2 != 0]
even_seq = [int(i) for i in input().split(sep=" ") if i%2 == 0]


def numerical_nuggets(seq1: list[int], seq2: list[int]) -> list[int]:
    new_list = seq1+ seq2
    new_list_sort = new_list.sort(reverse = True)

    return new_list_sort

output = numerical_nuggets(odd_seq, even_seq)
print(output)