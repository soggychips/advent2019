from lib import get_input


def prep_data():
    data = get_input(3)
    wire1 = data[0].split(',')
    wire2 = data[1].split(',')
    data = [wire1, wire2]
    return data


if __name__ == '__main__':
    data = prep_data()
    _map = {}
    L = 0
    for wire in data:
        for instr in wire:
            d = int(instr[1:])
            if d > L:
                L = d
    print(L)
