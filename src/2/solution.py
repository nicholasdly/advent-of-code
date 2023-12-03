import re
import math

LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def part_one(data: list[str]):
    total = len(data) * (len(data) + 1) // 2
    for id, game in enumerate(data, 1):
        for quantity, color in re.findall(r"(\d+) (\w+)", game):
            if int(quantity) > LIMITS[color]:
                total -= id
                break
    return total

def part_two(data: list[str]):
    total = 0
    for game in data:
        dice: dict[str, int] = {}
        for quantity, color in re.findall(r"(\d+) (\w+)", game):
            dice[color] = max(dice.get(color, int(quantity)), int(quantity))
        total += math.prod(dice.values())
    return total