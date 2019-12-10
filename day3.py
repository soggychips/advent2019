from lib import get_input

def part1():
    wires, d = [], {}
    wires.extend(list(map(lambda wire: wire.split(','), get_input(3))))
    for i, wire in enumerate(wires):
        x = y = 0
        for instruction in wire:
            direction, distance = instruction[0], int(instruction[1:])
            if direction in ('L', 'R'):
                delta = (1 if direction == 'R' else -1, 0)
            else:
                delta = (0, 1 if direction == 'U' else -1)
            for _ in range(distance):
                x += delta[0]
                y += delta[1]
                if (x,y) not in d:
                    d[(x,y)] = {'seen': set(), 'm_dist': abs(x) + abs(y)}
                d[(x,y)]['seen'].add(i)
    
    intersections = list(filter(lambda coord: len(coord[1]['seen']) > 1, d.items()))
    return min(map(lambda coord: coord[1]['m_dist'], intersections))
    
def part2():
    wires, d = [], {}
    wires.extend(list(map(lambda wire: wire.split(','), get_input(3))))
    for i, wire in enumerate(wires):
        x = y = steps = 0
        for instruction in wire:
            direction, distance = instruction[0], int(instruction[1:])
            if direction in ('L', 'R'):
                delta = (1 if direction == 'R' else -1, 0)
            else:
                delta = (0, 1 if direction == 'U' else -1)
            for _ in range(distance):
                steps += 1
                x += delta[0]
                y += delta[1]
                if (x,y) not in d:
                    d[(x,y)] = {'seen': set(), 'steps': {i: steps}}
                if i not in d[(x,y)]['steps']:
                    d[(x,y)]['steps'][i] = steps
                d[(x,y)]['seen'].add(i)
    
    intersections = list(filter(lambda coord: len(coord[1]['seen']) > 1, d.items()))
    return min(map(lambda coord: sum(coord[1]['steps'].values()), intersections))


if __name__ == '__main__':
    print(part1())
    print(part2())
