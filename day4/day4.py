#!/usr/bin/env python3

import re

EXAMPLE_ANSWER = [13, 2286]
RUN_EXAMPLE = True
RUN_INPUT = True


def solve_p1(puzzle: list[str]):
    "Part 1"

    score = 0
    for line in puzzle:
        regex_groups = re.match(r"Card\s+(\d+):([\s\d]+)\|([\s\d]+)", line)
        if regex_groups is None:
            print(f"No match in string: {line}")
            continue
        card_num, winning_line, have_line = (
            regex_groups.groups()[0],
            regex_groups.groups()[1],
            regex_groups.groups()[2],
        )
        winning = set([int(n) for n in re.findall(r"\d+", winning_line)])
        have = set([int(n) for n in re.findall(r"\d+", have_line)])
        matches = len(winning.intersection(have))
        # print(f"Matches: {matches} ({2 ** (matches -1)})")
        if matches > 0:
            score += 2 ** (matches - 1)
    return score


def solve_p2(puzzle: list[str]):
    "Part 2"

    return None


def solve_file(filename):
    "Solve both parts for a given file"
    with open(filename, "r", encoding="utf-8") as fh:
        lines = fh.readlines()
    return [solve_p1(lines), solve_p2(lines)]


if __name__ == "__main__":
    if RUN_EXAMPLE:
        example_result = solve_file("example.txt")
        print(
            f"Example part 1, got {example_result[0]} "
            f"with correct answer {EXAMPLE_ANSWER[0]}\n"
            f"Example part 2, got {example_result[1]} "
            f"with correct answer {EXAMPLE_ANSWER[1]}"
        )

    if RUN_INPUT:
        input_result = solve_file("input.txt")
        print(
            f"Input part 1, got {input_result[0]}\n"
            f"Input part 2, got {input_result[1]}"
        )
