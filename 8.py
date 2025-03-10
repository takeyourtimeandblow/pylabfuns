def tic_tac_toe(field):
    if "x x x" in field:
        return "x win"
    if "o o o" in field:
        return "o win"
    for i in range(0,field[0], 2):
        mark = field[0][i]
        if i == 2:
            if field[1][2] == mark and field[2][2] == mark:
                return mark + " win"



data = [
    "x x 0",
    "0 x 0",
    "x 0 0"
]
print(tic_tac_toe(data))