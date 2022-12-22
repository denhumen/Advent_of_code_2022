"""
Day5_1
"""

BOXES = [
    ['B', 'Z', 'T'],
    ['V', 'H', 'T', 'D', 'N'],
    ['B', 'F', 'M', 'D'],
    ['T', 'J', 'G', 'W', 'V', 'Q', 'L'],
    ['W', 'D', 'G', 'P', 'V', 'F', 'Q', 'M'],
    ['V', 'Z', 'Q', 'G', 'H', 'F', 'S'],
    ['Z', 'S', 'N', 'R', 'L', 'T', 'C', 'W'],
    ['Z', 'H', 'W', 'D', 'J', 'N', 'R', 'M'],
    ['M', 'Q', 'L', 'F', 'D', 'S']
]

BOXES1 = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']
]

def move_boxes(path: str, boxes: list) -> str:
    """
    (str, list) -> str

    Function finds some orders
    how to move boxes in file
    with path path and returns string
    with all last elements in each part
    of box list boxes
    """
    for list_ in boxes:
        list_.reverse()
    with open(path, 'r', encoding='utf-8') as input_file:
        lines = [x.strip() for x in input_file.readlines()]
    for line in lines:
        words = line.split()
        from_ = int(words[3]) - 1
        to_ = int(words[5]) - 1
        count = int(words[1])
        boxes_to_move = boxes[from_][:count]
        boxes[from_] = boxes[from_][count:]
        boxes_to_move.reverse()
        boxes[to_] = boxes_to_move + boxes[to_]
    answer = ''
    for x in boxes:
        answer += x[0]
    return answer

#print(move_boxes('input.txt', BOXES))