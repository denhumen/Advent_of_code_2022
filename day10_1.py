"""
Day10_1
"""

def count_signal(path: str) -> int:
    """
    str -> int

    Function calculates
    signal
    """
    with open(path, 'r', encoding='utf-8') as input_file:
        data = [x.strip() for x in input_file.readlines()]
    ans = 0
    x = 1
    cycle = 0
    for line in data:
        words = line.split()
        if words[0] == 'noop':
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                ans += x*cycle
        elif words[0] == 'addx':
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                ans += x*cycle
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                ans += x*cycle
            x += int(words[1])
    return ans
    
#print(count_signal('input.txt'))
