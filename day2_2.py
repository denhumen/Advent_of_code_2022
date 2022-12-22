"""
Day2_2
"""

# A - камінь (1)
# B - папір (2)
# C - ножиці (3)
# X - програти
# Y - нічия
# Z - виграти

def find_winner(path: str) -> int:
    """
    str -> int

    Function opens and reads file
    with path path and returns score
    of the player after doing everything
    that was written in the file
    """
    with open(path, 'r', encoding='utf-8') as input_file:
        data = [(x[0], x[2]) for x in input_file.readlines()]
    score = 0
    for play in data:
        if play[0] == 'A':
            if play[1] == 'X':
                score += 3
            elif play[1] == 'Y':
                score += 3
                score += 1
            else:
                score += 6
                score += 2
        elif play[0] == 'B':
            if play[1] == 'X':
                score += 1
            elif play[1] == 'Y':
                score += 3
                score += 2
            else:
                score += 6
                score += 3
        else:
            if play[1] == 'X':
                score += 2
            elif play[1] == 'Y':
                score += 3
                score += 3
            else:
                score += 6
                score += 1
    return score
    
#print(find_winner('input.txt'))
