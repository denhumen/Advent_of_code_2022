"""
Day2_1
"""

# A, X - камінь
# B, Y - папір
# C, Z - ножиці

def find_winner(path: str):
    """
    str -> int

    Function opens and reads file
    with path path and returns score
    of the player after doing everything
    that was written in the file
    """
    with open(path, 'r', encoding='utf-8') as input_file:
        data = [(x[0], x[2]) for x in input_file.readlines()]
    player1 = 0
    player2 = 0
    for play in data:
        if play[0] == 'A':
            player1 += 1
            if play[1] == 'X':
                player2 += 1
                player1 += 3
                player2 += 3
            elif play[1] == 'Y':
                player2 += 2
                player2 += 6
            else:
                player2 += 3
                player1 += 6
        elif play[0] == 'B':
            player1 += 2
            if play[1] == 'X':
                player2 += 1
                player1 += 6
            elif play[1] == 'Y':
                player2 += 2
                player1 += 3
                player2 += 3
            else:
                player2 += 3
                player2 += 6
        else:
            player1 += 3
            if play[1] == 'X':
                player2 += 1
                player2 += 6
            elif play[1] == 'Y':
                player2 += 2
                player1 += 6
            else:
                player2 += 3
                player1 += 3
                player2 += 3
    return player2

#print(find_winner('input.txt'))
