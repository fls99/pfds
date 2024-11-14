num_int = int(input())
unique_chars = set() 
for i in range(0,num_int):
    line = list(input()) 
    unique_chars.update(line) 
print(''.join(sorted(unique_chars, reverse=True)))



