"""
Day8_1
"""

def find_visible_trees(path: str):
    """
    str -> int

    Function finds the best place
    to build elf's tree-house
    """
    with open(path, 'r', encoding='utf-8') as input_file:
        data = input_file.readlines()
    map = []
    for line in data:
        elements = []
        for i in line.strip():
            elements.append(int(i))
        map.append(elements)
    counter = 0
    list_ = []
    for row in range(len(map)):
        for column in range(len(map[0])):
            if (row == 0 or column == 0 or
                row == (len(map) - 1) or column == (len(map[0]) - 1)):
                continue
            elem = map[row][column]
            if all(map[row][i] < elem for i in range(column + 1, len(map[0]))):
                list_.append((row, column))
                counter += 1
            elif all(map[row][i] < elem for i in range(0, column)):
                counter += 1
                list_.append((row, column))
            elif all(map[i][column] < elem for i in range(row + 1, len(map))):
                counter += 1
                list_.append((row, column))
            elif all(map[i][column] < elem for i in range(0, row)):
                counter += 1
                list_.append((row, column))
    return counter + 2 * (len(map) + len(map[0]) - 2)

#print(find_visible_trees('input.txt'))
