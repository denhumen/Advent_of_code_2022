"""
Day10_2
"""

def count_signal(path: str) -> int:
    """
    str -> int

    Function calculates
    signal
    """
    with open(path, 'r', encoding='utf-8') as input_file:
        data = [x.strip() for x in input_file.readlines()]
    field = [['?' for _ in range(40)] for i in range(6)]
    ans = 0
    x = 1
    cycle = -1
    for line in data:
        words = line.split()
        if words[0] == 'noop':
            cycle += 1
            field[cycle//40][cycle%40] = ("#" if abs(x-(cycle%40)) <= 1 else " ")
            if cycle in [20, 60, 100, 140, 180, 220]:
                ans += x*cycle
        elif words[0] == 'addx':
            cycle += 1
            field[cycle//40][cycle%40] = ("#" if abs(x-(cycle%40)) <= 1 else " ")
            if cycle in [20, 60, 100, 140, 180, 220]:
                ans += x*cycle
            cycle += 1
            field[cycle//40][cycle%40] = ("#" if abs(x-(cycle%40)) <= 1 else " ")
            if cycle in [20, 60, 100, 140, 180, 220]:
                ans += x*cycle
            x += int(words[1])
    for i in range(6):
        print("".join(field[i]))

count_signal('input.txt')
