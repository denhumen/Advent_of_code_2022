"""
Day3_2
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
    for i in range(0, len(data), 3):
        x = data[i].strip()
        y = data[i+1].strip()
        z = data[i+2].strip()
        for i in x:
            if i in y and i in z:
                if 'a' <= i <= 'z':
                    counter += ord(i) - ord('a') + 1
                else:
                    counter += ord(i) - ord('A') + 27
                break
    return counter

#print(backpack('input.txt'))
