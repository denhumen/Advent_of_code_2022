"""
Day11_1
"""

def monkey_bussiness(path: str) -> int:
    """
    str -> int

    Function calculates
    monkey bussiness
    """
    with open(path, 'r', encoding='utf-8') as input_file:
        data = [x for x in input_file.read().split('\n\n')]
    monkeys = dict()
    ops = []
    T = []
    TRUE = []
    FALSE = []
    for monkey in data:
        id_, items, op, test, true, false = monkey.split('\n')
        m_id = int(id_[:-1].split()[1])
        if m_id not in monkeys:
            monkeys[m_id] = []
        monkeys[m_id] = [int(x) for x in items.split(':')[1].split(',')]
        words = op.split()
        op = ''.join(words[-3:])
        ops.append(lambda old, op=op: eval(op))
        T.append(int(test.split()[-1]))
        TRUE.append(int(true.split()[-1]))
        FALSE.append(int(false.split()[-1]))
    C = [0 for i in range(len(monkeys))]
    for _ in range(20):
        for i in range(len(monkeys)):
            for item in monkeys[i]:
                C[i] += 1
                item = ops[i](item)
                item = (item // 3)
                if item % T[i] == 0:
                    monkeys[TRUE[i]].append(item)
                else:
                    monkeys[FALSE[i]].append(item)
            monkeys[i] = []
    return sorted(C)[-1] * sorted(C)[-2]

#print(monkey_bussiness('input.txt'))
