#!/usr/bin/env python3

import regex as re

example_answer = [142, 281]


def solve(input: list[str]):
    return None
    sum = 0
    for line in input:
        digits = re.findall(r"\d", line)
        sum += int(digits[0] + digits[-1])
    return sum


def cast(s: str):
    match s:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"
        case _:
            return s


def solve2(input: list[str]):
    sum = 0
    for line in input:
        digits = re.findall(
            r"\d|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True
        )
        d1 = cast(digits[0])
        d2 = cast(digits[-1])
        sum += int(d1 + d2)
    return sum


def solve_file(filename) -> [any, any]:
    with open(filename, "r") as fh:
        input = fh.readlines()
    return [solve(input), solve2(input)]


if __name__ == "__main__":
    example_result = solve_file("example.txt")
    print(
        f"Example part 1, got {example_result[0]} with correct answer {example_answer[0]}\n"
        f"Example part 2, got {example_result[1]} with correct answer {example_answer[1]}"
    )

    input_result = solve_file("input.txt")
    print(
        f"Input part 1, got {input_result[0]}\n" f"Input part 2, got {input_result[1]}"
    )
