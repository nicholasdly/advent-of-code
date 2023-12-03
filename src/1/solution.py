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

def part_one(data: str):
    lines = [list(filter(str.isdigit, line)) for line in data.splitlines()]
    return sum([int(nums[0] + nums[-1]) for nums in lines])

def part_two(data: str):
    pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))"
    lines = [re.findall(pattern, line) for line in data.splitlines()]

    total = 0
    for nums in lines:
        first = NUMBER_STRINGS[nums[0]] if nums[0] in NUMBER_STRINGS else nums[0]
        last = NUMBER_STRINGS[nums[-1]] if nums[-1] in NUMBER_STRINGS else nums[-1]
        total += int(first + last)
    return total