import os
import time
import re

NUMBER_STRINGS = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

def part_one(data: str) -> int:
    """
    Reads every line of the input data, removing all non-numeric characters.
    Returns the sum of all numbers created by concatenating the first and last
    digits of every line.
    """
    lines = [list(filter(str.isdigit, line)) for line in data.splitlines()]
    return sum([int(nums[0] + nums[-1]) for nums in lines])

def part_two(data: str):
    """
    Reads every line of the input data, extracting all digits and spelled out
    digits. Returns the sum of all numbers created by concatenating the first
    and last digits (including digits spelled out) of every line.
    """
    pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))"
    lines = [re.findall(pattern, line) for line in data.splitlines()]

    total = 0
    for nums in lines:
        first = NUMBER_STRINGS[nums[0]] if nums[0] in NUMBER_STRINGS else nums[0]
        last = NUMBER_STRINGS[nums[-1]] if nums[-1] in NUMBER_STRINGS else nums[-1]
        total += int(first + last)
    return total

def read_input(filename: str) -> str:
    """
    Reads and returns the contents of a specified input text file.
    """
    input_path = os.path.join(os.path.dirname(__file__), f"input/{filename}")
    with open(input_path) as file:
        return file.read()

if __name__ == "__main__":
    data = read_input("input.txt")

    t1 = time.perf_counter()
    print(part_one(data))
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.6f} seconds.")

    t1 = time.perf_counter()
    print(part_two(data))
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.6f} seconds.")
