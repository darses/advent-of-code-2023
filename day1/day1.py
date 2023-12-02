#!/usr/bin/env python3

import re

example_answer = 142


def solve(input):
    sum = 0
    for line in input:
        digits = re.findall(r"\d", line)
        sum += int(digits[0] + digits[-1])
    return sum


def solve_file(filename):
    with open(filename, "r") as fh:
        input = fh.readlines()
    return solve(input)


if __name__ == "__main__":
    example_result = solve_file("example.txt")
    if solve_file("example.txt") == example_answer:
        print("Example success, computing result for input.txt")
        print(f'Result: {solve_file("input.txt")}')
    else:
        print(f"Example failed, got {example_result} instead of {example_answer}")
