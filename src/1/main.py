import os
import time

from solution import part_one, part_two

def read_input(filename: str) -> str:
    input_path = os.path.join(os.path.dirname(__file__), f"input/{filename}")
    with open(input_path) as file:
        return file.read()

if __name__ == "__main__":
    t1 = time.perf_counter()
    data = read_input("input.txt")
    t2 = time.perf_counter()
    print(f"Input processing time: {t2 - t1:0.6f} seconds.")

    t1 = time.perf_counter()
    print(part_one(data))
    t2 = time.perf_counter()
    print(f"Part one execution time: {t2 - t1:0.6f} seconds.")

    t1 = time.perf_counter()
    print(part_two(data))
    t2 = time.perf_counter()
    print(f"Part two execution time: {t2 - t1:0.6f} seconds.")
