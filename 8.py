def tic_tac_toe(field):
    if "x x x" and "o o o" in field:
        return "someone is cheating! draw"
    if "x x x" in field:
        return "x win"
    if "o o o" in field:
        return "o win"
    nested_field = [i.split(' ') for i in field]
    for i in range(len(nested_field[0])):
        match i:
            case 0:
                if nested_field[0][0] == nested_field[1][1] == nested_field[2][2]:
                    return nested_field[0][0] + "win"
            case 2:
                if nested_field[0][2] == nested_field[1][1] == nested_field[2][0]:
                    return nested_field[0][2] + "win"
    vertical0 = ''.join([i[0] for i in nested_field])
    vertical1 = ''.join([i[1] for i in nested_field])
    vertical2 = ''.join([i[2] for i in nested_field])
    vertical_iter = [vertical0, vertical1, vertical2]
    if "xxx" in vertical_iter:
        return "x win"
    if "ooo" in vertical_iter:
        return "o win"

data = [
    "x x o",
    "o x o",
    "x o o"
]
print(tic_tac_toe(data))