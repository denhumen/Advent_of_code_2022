"""
Day4_1
"""

def find_includes(path: str) -> int:
    """
    str -> int

    Function reads file and returns
    count of diapasons that containes 
    another diapason
    """
    parts = []
    with open(path, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()
        for line in lines:
            diapasons = line.strip().split(',')
            for d in diapasons:
                parts.append(tuple(d.split('-')))
    counter = 0
    for i in range(0, len(parts), 2):
        a = int(parts[i][0])
        b = int(parts[i][1])
        c = int(parts[i+1][0])
        d = int(parts[i+1][1])
        if (a >= c and b <= d) or (a <= c and b >= d):
            counter += 1
    return counter

#print(find_includes('input.txt'))
