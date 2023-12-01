import os
import time

def part_one(data: str):
    return 2

def part_two(data: str):
    return 4

def get_input() -> str:
    input_path = os.path.join(os.path.dirname(__file__), "input/input.txt")
    with open(input_path) as file:
        return file.read()

if __name__ == "__main__":
    data = get_input()

    t1 = time.perf_counter()
    print(part_one(data))
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.5f} seconds.")

    t1 = time.perf_counter()
    print(part_two(data))
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.5f} seconds.")
