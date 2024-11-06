
import string

send = input().lower().translate(str.maketrans('', '', string.punctuation)).split(sep=" ")
ref = input().lower().translate(str.maketrans('', '', string.punctuation)).split(sep=" ")


def secrets_in_the_sands(send:list[str], ref:list[str]) -> bool:

    # check if a word of senders in reference
    if any(item in ref for item in send):
        return False
    else:
        return True

output = secrets_in_the_sands(send, ref)
print(output)