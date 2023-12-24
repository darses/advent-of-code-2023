#!/usr/bin/env python3

EXAMPLE_ANSWER = [8, 2286]
RUN_EXAMPLE = True
RUN_INPUT = True


def solve_p1(input: list[str]):
    "Part 1"
    return None


def solve_p2(input: list[str]):
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
