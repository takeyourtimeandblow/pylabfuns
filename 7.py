def palindrome(text):
    text = text.replace(" ", '')
    text = text.lower()
    if text == text[::-1]:
        return True
    return False


print(palindrome("А роза упала на лапу азора"))