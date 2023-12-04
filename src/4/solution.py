from dataclasses import dataclass
import re

@dataclass
class Scratchcard:
    quantity: int
    numbers: set[int]
    winning: set[int]

def part_one(data: str):
    total = 0
    scratchcards = _parse_data(data)
    for card in scratchcards:
        matches = len(card.winning.intersection(card.numbers))
        if matches > 0:
            total += 2 ** (matches - 1)
    return total

def part_two(data: str):
    total = 0
    scratchcards = _parse_data(data)
    for index, card in enumerate(scratchcards):
        total += card.quantity
        matches = len(card.winning.intersection(card.numbers))
        for i in range(1, matches + 1):
            scratchcards[index + i].quantity += card.quantity
    return total

def _parse_data(data: str) -> list[Scratchcard]:
    scratchcards: list[Scratchcard] = []
    
    for line in data.splitlines():
        line = re.sub(r"Card\s+\d+:", '', line)  # Remove card header
        winning_numbers, card_numbers = line.split('|')  # Separate winning numbers from card numbers

        # Populate collection of scratchcards
        card = Scratchcard(
            quantity=1,
            winning=set(int(n) for n in winning_numbers.split()),
            numbers=set(int(n) for n in card_numbers.split())
        )
        scratchcards.append(card)

    return scratchcards
