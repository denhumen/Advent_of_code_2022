"""
Day3_1
"""

def backpack(path: str) -> int:
    """
    str -> int

    Function reads file with path path
    and returns count of letter indexes
    """
    with open(path, 'r', encoding='utf-8') as input_file:
        data = input_file.readlines()
    counter = 0
    for line in data:
        x = line.strip()
        y, z = x[:len(x)//2], x[len(x)//2:]
        print(x, y, z)
        for i in y:
            if i in z:
                if 'a' <= i <= 'z':
                    counter += ord(i) - ord('a') + 1
                else:
                    counter += ord(i) - ord('A') + 27
                break
    return counter

#print(backpack('input.txt'))
