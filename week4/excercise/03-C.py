inp = [int(i) for i in input().split()]
T = int(input())
x = 'Foo'
for i, num in enumerate(inp):
    if num >= T:
        x = i
        break
print(x)


    
