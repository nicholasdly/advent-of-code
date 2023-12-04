import re

def part_one(schematic: list[list[str]]):

    # Save all possible part numbers, remove them as they are validated to
    # prevent the same number from being added multiple times to the sum of all
    # valid part numbers.
    unvisited: list[int] = []
    for line in schematic:
        unvisited += [int(value) for value in re.findall(r"\d+", "".join(line))]

    total = 0
    for row, line in enumerate(schematic):
        for column, character in enumerate(line):

            if character == '.' or character.isdigit():
                continue

            north, south, west, east = None, None, None, None
            northwest, northeast, southwest, southeast = None, None, None, None

            # Retrieves part number to the north, northwest, and northeast of
            # the symbol if it exsists.
            if row > 0:
                north = _digit_scan(schematic[row - 1], column)
                if north is None and column > 0:
                    northwest = _digit_scan(schematic[row - 1], column - 1)
                if north is None and column < len(line) - 1:
                    northeast = _digit_scan(schematic[row - 1], column + 1)

            # Retrieves part number to the south, southwest, and southeast of
            # the symbol if it exsists.
            if row < len(schematic) - 1:
                south = _digit_scan(schematic[row + 1], column)
                if south is None and column > 0:
                    southwest = _digit_scan(schematic[row + 1], column - 1)
                if south is None and column < len(line) - 1:
                    southeast = _digit_scan(schematic[row + 1], column + 1)

            # Retrieves part number to the west of the symbol if it exists.
            if column > 0:
                west = _digit_scan(line, column - 1)

            # Retrieves part number to the east of the symbol if it exists
            if column < len(line) - 1:
                east = _digit_scan(line, column + 1)

            # Computes the sum of all valid part numbers.
            for value in (north, south, west, east, northwest, northeast, southwest, southeast):
                if value is not None and value in unvisited:
                    total += value
                    unvisited.remove(value)
    
    return total

def part_two(schematic: list[list[str]]):

    # Save all possible part numbers, remove them as they are validated to
    # prevent the same number from being added multiple times to the sum of all
    # valid part numbers.
    unvisited: list[int] = []
    for line in schematic:
        unvisited += [int(value) for value in re.findall(r"\d+", "".join(line))]

    total = 0
    for row, line in enumerate(schematic):
        for column, character in enumerate(line):

            if character != '*':
                continue

            north, south, west, east = None, None, None, None
            northwest, northeast, southwest, southeast = None, None, None, None

            # Retrieves part number to the north, northwest, and northeast of
            # the symbol if it exsists.
            if row > 0:
                north = _digit_scan(schematic[row - 1], column)
                if north is None and column > 0:
                    northwest = _digit_scan(schematic[row - 1], column - 1)
                if north is None and column < len(line) - 1:
                    northeast = _digit_scan(schematic[row - 1], column + 1)

            # Retrieves part number to the south, southwest, and southeast of
            # the symbol if it exsists.
            if row < len(schematic) - 1:
                south = _digit_scan(schematic[row + 1], column)
                if south is None and column > 0:
                    southwest = _digit_scan(schematic[row + 1], column - 1)
                if south is None and column < len(line) - 1:
                    southeast = _digit_scan(schematic[row + 1], column + 1)

            # Retrieves part number to the west of the symbol if it exists.
            if column > 0:
                west = _digit_scan(line, column - 1)

            # Retrieves part number to the east of the symbol if it exists
            if column < len(line) - 1:
                east = _digit_scan(line, column + 1)

            # Computes the sum of all gear ratios.
            part_numbers = [north, south, west, east, northwest, northeast, southwest, southeast]
            part_numbers = [value for value in part_numbers if value is not None]

            if len(part_numbers) != 2:
                continue

            total += part_numbers[0] * part_numbers[1]
            for value in part_numbers:
                unvisited.remove(value)
    
    return total

def _digit_scan(line: list[str], index: int) -> int | None:
    """
    Returns an `int` formed by horizontally adjacent digits of a string at a
    specified `index` of the string. If there are no digits at `index`, returns
    `None` sicne there does not exist a number.
    """
    if not line[index].isdigit():
        return None

    number = line[index]

    for character in line[index - 1::-1]:
        if not character.isdigit():
            break
        number = character + number

    for character in line[index + 1:]:
        if not character.isdigit():
            break
        number += character

    return int(number)
