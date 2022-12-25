"""
Day6_2
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
            check_list = []
            for j in range(i, i+14):
                check_list.append(line[j])
            if uniq_check(check_list):
                return i+14

def uniq_check(ls: list) -> bool:
    """
    list -> bool

    Function checks if
    list includes only
    unique elements
    """
    for i in range(len(ls)):
        for j in range(len(ls)):
            if i != j and ls[i] == ls[j]:
                return False
    return True

#print(find_marker('input.txt'))
