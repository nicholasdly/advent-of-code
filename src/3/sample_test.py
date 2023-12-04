from main import part_one, part_two, read_input

def test_part_one():
    print()
    data = read_input("sample_input.txt")
    assert part_one(data) == 4361

def test_part_two():
    data = read_input("sample_input.txt")
    assert part_two(data) == 467835
