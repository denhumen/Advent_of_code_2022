"""
Day8_1
"""

def find_visible_trees(path: str) -> int:
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
    max_sum = 0
    list_ = dict()
    list2 = []
    for row in range(len(map)):
        for column in range(len(map[0])):
            if (row == 0 or column == 0 or
                row == (len(map) - 1) or column == (len(map[0]) - 1)):
                continue
            element = map[row][column]
            up = [map[i][column] for i in range(row+1, len(map))]
            down = [map[i][column] for i in range(0, row)]
            down.reverse()
            right = [map[row][i] for i in range(column+1, len(map[0]))]
            left = [map[row][i] for i in range(0, column)]
            left.reverse()
            sides = [up, down, right, left]
            visibility = 1
            list2.append(sides)
            for side in sides:
                counter = 0
                for i in side:
                    if i < element:
                        counter += 1
                    elif i >= element:
                        counter += 1
                        break
                visibility *= counter
            if visibility >= max_sum:
                max_sum = visibility
            list_[(row, column)] = visibility
    return max_sum

#print(find_visible_trees('input.txt'))
