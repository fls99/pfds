rstr = input().replace(" ", "")
unique_chr = set(rstr)
melody = {f"{char}": rstr.count(char) for i, char in enumerate(unique_chr)}
print(dict(sorted(melody.items())))
