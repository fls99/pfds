l_input = int(input())
seq = [int(input()) for i in range(0,l_input)]
for i, num in enumerate(seq):
    if i%3 == 0:
        seq[i] = "fizz"
    if i%5 == 0:
        seq[i] = 'buzz'
    if i%5 == 0 and i%3 == 0:
        seq[i] = 'FizzBuzz'
    
print(seq)



