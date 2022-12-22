"""
Day1_2
"""

def count_calories(path : str) -> int:
    """
    str -> int

    Finds the sum of calories
    that have the best 3 elfs
    """
    answer = []
    with open(path, 'r', encoding='utf-8') as input_file:
        count = 0
        i = 1
        for elem in input_file.readlines():
            if elem == '\n':
                answer.append((i, count))
                count = 0
                i += 1
            else:
                count += int(elem.strip())
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    sum_ = 0
    for i in range(3):
        sum_ += answer[i][1]
    return sum_

#print(count_calories('input.txt'))
