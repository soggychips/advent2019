"""
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 367479-893698.

--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

Your puzzle input is still 367479-893698.
"""

puzzle_input = range(367479, 893699)

def num_only_increases(n):
    prev = None
    for digit in (int(x) for x in str(n)):
        if prev is not None:
            if digit < prev:
                return False
        prev = digit
    return True

def two_adj_exists(n):
    prev = None
    for digit in (int(x) for x in str(n)):
        if prev is not None:
            if digit == prev:
                return True
        prev = digit
    return False

def at_least_one_double_exists(n):
    n = str(n)
    d = {i: n.count(i) for i in n}
    return 2 in d.values()


def part1():
  return sum(map(lambda n: 1 if two_adj_exists(n) and num_only_increases(n) else 0, puzzle_input))

def part2():
    return sum(map(lambda n: 1 if at_least_one_double_exists(n) and num_only_increases(n) else 0, puzzle_input))

if __name__ == "__main__":
    print(part1())
    print(part2())