dict = {}

def add_friends(person, friends):
    if person in dict.keys():
        for i in friends:
            dict[person].add(i)
    else:
        dict[person] = set(friends)
    for i in friends:
        dict[i] = person


def are_friends(person1, person2):
    if person1 in dict[person2] and person2 in dict[person1]:
        return True
    return False

def print_friends(person):
    print(dict[person])


add_friends("Artem", ["Egor", "Timofei"])
add_friends("Artem", ["Egor"])
add_friends("Artem", ["Evgeniy"])
print(are_friends("Artem", "Egor"))
print_friends("Artem")
print(dict)
