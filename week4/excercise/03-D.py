n = int(input())
m = int(input())
operator = input()

# create two lists of same length
int_list_a = [i for i in range(1,n+1)]
int_list_b = [ i for i in range((m-n+1), m+1)]

# define operator dict with lambda function
op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x,y: x * y,
      '/': lambda x,y: x / y
      }

new_list = [op[operator](i,j) for i, j in zip(int_list_a, int_list_b)]


print(sum(new_list)/len(new_list))
