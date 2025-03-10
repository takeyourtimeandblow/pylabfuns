def is_brackets_closed(text):
    while text:
        if '()' not in text:
            return False
        text = text.replace('()', '')
    return True


print(is_brackets_closed("(()()(())"))