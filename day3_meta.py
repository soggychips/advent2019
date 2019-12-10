from lib import get_input
from collections import namedtuple
from itertools import chain

Line = namedtuple('Line', 'x1 x2 y1 y2')
Point = namedtuple('Point', 'x y')

def prep_wires():
    data = get_input(3)
    wire1 = data[0].split(',')
    wire2 = data[1].split(',')
    data = [wire1, wire2]
    return data

def parse_instruction(i):
    # returns (dx, horizontal)
    direction, distance = i[0], int(i[1:])
    if direction == 'R':
        return ((distance, 0), 1)
    elif direction == 'L':
        return ((-1*distance, 0), 1)
    elif direction == 'D':
        return ((0, -1*distance), 0)
    elif direction == 'U':
        return ((0, distance), 0)

def prep_data():
    data = []
    data.extend(list(map(lambda wire: wire.split(','), get_input(3))))
    h_lines, v_lines = [], []
    x,y = 0,0
    for line in chain(data[0], data[1]):
        print(line)
        (x2,y2), horizontal = parse_instruction(line)
        if horizontal:
            h_lines.append(Line(x, x2, y, y2))
        else:
            v_lines.append(Line(x, x2, y, y2))
        x = x2
        y = y2
    return h_lines, v_lines

def lines_intersect(line1, line2):
    #return False if false, or a point where true
    # ta=(y3−y4)(x1−x3)+(x4−x3)(y1−y3)/(x4−x3)(y1−y2)−(x1−x2)(y4−y3)
    # tb=(y1−y2)(x1−x3)+(x2−x1)(y1−y3)(x4−x3)(y1−y2)−(x1−x2)(y4−y3)
    ta = ((line2.y1 - line2.y2) * (line1.x1 - line2.x1) + (line2.x2 - line2.x1) * (line1.y1 - line2.y1)) / ((line2.x2 - line2.x1) * (line1.y1 - line1.y2) - (line1.x1 - line1.x2) * (line2.y2 - line2.y1))
    tb = ((line1.y1-line1.y2) * (line1.x1 - line2.x1) + (line1.x2 - line1.x1) * (line1.y1 - line2.y1)) / ((line2.x2 - line2.x1) * (line1.y1 - line1.y2) - (line1.x1 - line1.x2) * (line2.y2 - line2.y1))
    if (1 >= ta >= 0) and (1 >= tb >= 0):
        return True
    return False

if __name__ == '__main__':
    h_lines, v_lines = prep_data()
    print(h_lines)
    # data = prep_wires()
    # _map = {}
    # L = 0
    # for wire in data:
    #     for instr in wire:
    #         d = int(instr[1:])
    #         if d > L:
    #             L = d
    # print(L)
