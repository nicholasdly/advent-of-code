from main import part_one, part_two, read_input

def test_part_one():
    data = read_input("sample_input.txt")
    assert part_one(data) == 8

def test_part_two():
    data = read_input("sample_input.txt")
    assert part_two(data) == 2286
