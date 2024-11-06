import re
import string

rstr = input().lower()

def palindrome_checker(rstr: str) -> bool:
    """
    Cleans a string of all whitespaces and punctuations.
    Then checks if the word is a palindrom.

    @param rstr: A random string
    @return: Return True or False if string is a palindrom
    """
    clean_string: str = rstr.replace(" ", "").translate(str.maketrans('', '', string.punctuation))
    reversed_string: str = clean_string[::-1]

    if clean_string == reversed_string:
        return True
    else:
        return False

output = palindrome_checker(rstr)
print(output)