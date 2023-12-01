import time

def part_one():
    return 2

def part_two():
    return 4

def main():
    print("Hello world!")

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.5f} seconds.")
