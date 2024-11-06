seq1 = [int(i) for i in input().split(sep=" ")]
seq2 = [int(i) for i in input().split(sep=" ")]


def numerical_nuggets(seq1: list[int], seq2: list[int]) -> list[int]:
    odd_seq = [i for i in seq1 if i%2 != 0]
    even_seq = [i for i in seq2 if i%2 == 0]

    new_list = odd_seq + even_seq
    new_list_sort = new_list.sort(reverse = True)

    return new_list

output = numerical_nuggets(seq1, seq2)
print(output)