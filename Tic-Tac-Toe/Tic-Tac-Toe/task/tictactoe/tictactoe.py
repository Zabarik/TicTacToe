cells_list = list("_________")


def print_cells():
    print("---------")
    print("|", cells_list[0], cells_list[1], cells_list[2], "|")
    print("|", cells_list[3], cells_list[4], cells_list[5], "|")
    print("|", cells_list[6], cells_list[7], cells_list[8], "|")
    print("---------")


def take_coordinates():
    crs = input("Enter the coordinates:").split()
    while len(crs) != 2 or not crs[0].isdecimal() or not crs[1].isdecimal():
        print("You should enter numbers!")
        crs = input("Enter the coordinates:").split()
    crs = [int(x) for x in crs]
    return crs


def place_coordinates(crs, move):
    if crs[0] not in range(1, 4) or crs[1] not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
        return False
    if crs[0] == 1:
        cells_column = (0, 3, 6)
    elif crs[0] == 2:
        cells_column = (1, 4, 7)
    else:
        cells_column = (2, 5, 8)
    if crs[1] == 1:
        cells_row = (6, 7, 8)
    elif crs[1] == 2:
        cells_row = (3, 4, 5)
    else:
        cells_row = (0, 1, 2)
    cell = 0
    for i in range(9):
        if i in cells_row and i in cells_column:
            cell = i
            break
    if cells_list[cell] != "_":
        print("This cell is occupied! Choose another one!")
        return False
    else:
        cells_list[cell] = move
        return True


def check_results():
    cells = "".join(cells_list)
    straights = [cells[:3], cells[3:6], cells[6:], cells[0:7:3], cells[1:8:3], cells[2:9:3], cells[0:9:4], cells[2:7:2]]
    if abs(len([x for x in cells_list if x == "X"]) - len([x for x in cells_list if x == "O"])) > 1:
        print("Impossible")
    elif "XXX" in straights and "OOO" in straights:
        print("Impossible")
    elif "XXX" in straights:
        print("X wins")
    elif "OOO" in straights:
        print("O wins")
    elif len([x for x in cells_list if x == "_"]) > 0:
        # print("Game not finished")
        return False
    else:
        print("Draw")
    return True


print_cells()
is_finished = False
who_moves = "X"
while not is_finished:
    is_placed = False
    while not is_placed:
        coordinates = take_coordinates()
        is_placed = place_coordinates(coordinates, who_moves)
    if who_moves == "X":
        who_moves = "O"
    else:
        who_moves = "X"
    print_cells()
    is_finished = check_results()

