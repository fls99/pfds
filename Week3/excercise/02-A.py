from typing import Union

rstr = input()

def wordplay(rstr:str) -> Union[str, int]:
    """
    Return a new string based on two first and last chars 
    
    @param rstr: A random string
    @return: Return a 0 if len is below 2 or the new word
    """
    if len(rstr) < 2:
        return 0
    else:
        return rstr[:2] + rstr[-2:]

newword = wordplay(rstr)
print(newword)