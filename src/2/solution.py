import re
import math

LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def part_one(data: str):
    games = _parse_data(data)
    total = len(games) * (len(games) + 1) // 2
    for id, game in enumerate(games, 1):
        for quantity, color in re.findall(r"(\d+) (\w+)", game):
            if int(quantity) > LIMITS[color]:
                total -= id
                break
    return total

def part_two(data: str):
    games = _parse_data(data)
    total = 0
    for game in games:
        dice: dict[str, int] = {}
        for quantity, color in re.findall(r"(\d+) (\w+)", game):
            dice[color] = max(dice.get(color, int(quantity)), int(quantity))
        total += math.prod(dice.values())
    return total

def _parse_data(data: str) -> list[str]:
    return data.splitlines()
