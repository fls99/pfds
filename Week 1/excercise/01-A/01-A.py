some_str = input()

def reverse_string(some_str: str) -> str:
    """
    Reverses a valid string
    
    @some_str: str A random string
    @return Returns some string in reversed order
    """
    if isinstance(some_str, str):
        reversed_str: str = some_str[::-1]
        return reversed_str
    else:
        return print("Please type in a string")

reversed_str = reverse_string(some_str)

print(reverse_string)



