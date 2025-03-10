same = []
def print_without_duplicates(text):
    if text in same:
        return
    print(text)
    same.append(text)


print_without_duplicates("Cross")
print_without_duplicates("Cross")
print_without_duplicates("Cross")

