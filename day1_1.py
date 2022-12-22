"""
Day1_1
"""

def count_calories(path : str) -> list:
    """
    str -> list

    Function finds the amount of
    calories that has the best elf
    """
    with open(path, 'r', encoding='utf-8') as input_file:
        count = 0
        max_count = 0
        i = 1
        index = 0
        for elem in input_file.readlines():
            if elem == '\n':
                if count >= max_count:
                    max_count = count
                    index = i
                count = 0
                i += 1
            else:
                count += int(elem.strip())
    return (index, max_count)

#print(count_calories('input.txt'))
