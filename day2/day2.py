#!/usr/bin/env python3

import re

example_answer = [8, 2286]
run_example = True
run_input = True


def solve_p1(input: list[str]):
    games = []
    id = 0
    for line in input:
        id += 1
        # process all sets of cubes in a single game
        sets = []
        for set in line.split(": ")[1].split(";"):
            blue, red, green = 0, 0, 0
            # print(f"Set: {set}")
            for match in re.findall(r"\d+ blue|\d+ red|\d+ green", set):
                if "blue" in match:
                    blue = int(match.split(" ")[0])
                elif "green" in match:
                    green = int(match.split(" ")[0])
                elif "red" in match:
                    red = int(match.split(" ")[0])
            sets.append({"blue": blue, "green": green, "red": red})

        # Compute maximum number of cubes in the game, per color
        max_blue, max_green, max_red = 0, 0, 0
        for set in sets:
            if set["blue"] > max_blue:
                max_blue = set["blue"]
            if set["green"] > max_green:
                max_green = set["green"]
            if set["red"] > max_red:
                max_red = set["red"]
        games.append({"id": id, "blue": max_blue, "green": max_green, "red": max_red})

    # Which games are possible with only 12 red, 13 green, and 14 blue.
    solvable_games = []
    for game in games:
        if game["red"] <= 12 and game["green"] <= 13 and game["blue"] <= 14:
            solvable_games.append(int(game["id"]))

    # What is the sum of the IDs of those games?
    return sum(solvable_games)


def solve_p2(input: list[str]):
    games = []
    id = 0
    sum_power = 0
    for line in input:
        id += 1
        # process all sets of cubes in a single game
        sets = []
        for set in line.split(": ")[1].split(";"):
            blue, red, green = 0, 0, 0
            # print(f"Set: {set}")
            for match in re.findall(r"\d+ blue|\d+ red|\d+ green", set):
                if "blue" in match:
                    blue = int(match.split(" ")[0])
                elif "green" in match:
                    green = int(match.split(" ")[0])
                elif "red" in match:
                    red = int(match.split(" ")[0])
            sets.append({"blue": blue, "green": green, "red": red})

        # Compute maximum number of cubes in the game, per color
        max_blue, max_green, max_red = 0, 0, 0
        for set in sets:
            if set["blue"] > max_blue:
                max_blue = set["blue"]
            if set["green"] > max_green:
                max_green = set["green"]
            if set["red"] > max_red:
                max_red = set["red"]
        power = max_blue * max_green * max_red
        games.append(
            {
                "id": id,
                "blue": max_blue,
                "green": max_green,
                "red": max_red,
                "power": power,
            }
        )
        sum_power += power

    # What is the sum of the IDs of those games?
    return sum_power


def solve_file(filename) -> [any, any]:
    with open(filename, "r") as fh:
        input = fh.readlines()
    return [solve_p1(input), solve_p2(input)]


if __name__ == "__main__":
    if run_example:
        example_result = solve_file("example.txt")
        print(
            f"Example part 1, got {example_result[0]} with correct answer {example_answer[0]}\n"
            f"Example part 2, got {example_result[1]} with correct answer {example_answer[1]}"
        )

    if run_input:
        input_result = solve_file("input.txt")
        print(
            f"Input part 1, got {input_result[0]}\n"
            f"Input part 2, got {input_result[1]}"
        )
