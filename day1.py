from lib import get_input_via_requests as get_input


def part1():
    data = get_input(1)
    total_fuel_needed = 0
    for mass in data:
        total_fuel_needed += int(int(mass) / 3) - 2
    print(total_fuel_needed)


def part2():
    data = get_input(1)
    total_fuel_needed = 0
    for mass in data:
        incremental_fuel = int(int(mass) / 3) - 2
        while(incremental_fuel > 0):
            total_fuel_needed += incremental_fuel
            incremental_fuel = int(incremental_fuel / 3) - 2
    print(total_fuel_needed)


if __name__ == "__main__":
    part1()
    part2()
