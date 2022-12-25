"""
Day6_1
"""

def find_marker(path: str):
    """
    str -> int

    Function finds marker
    in elf's message
    """
    with open(path, 'r', encoding='utf-8') as input_file:
        data = input_file.readlines()
    for line in data:
        for i in range(len(line)):
            list_ = []
            list_.append(line[i])
            list_.append(line[i+1])
            list_.append(line[i+2])
            list_.append(line[i+3])
            if(list_.count(line[i]) == 1 and
                list_.count(line[i+1]) == 1 and
                list_.count(line[i+2]) == 1 and
                list_.count(line[i+3]) == 1):
                return i+4

#print(find_marker('input.txt'))
