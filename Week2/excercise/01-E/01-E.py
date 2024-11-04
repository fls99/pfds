
def determine_type(object_list: list) -> list:
    return [type(i) for i in object_list]

input = eval(input())
output = determine_type(input)
print(output)


