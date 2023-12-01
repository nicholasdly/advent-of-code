from main import part_one, part_two, read_input

def test_part_one():
    data = read_input("sample_input1.txt")
    assert part_one(data) == 142

def test_part_two():
    data = read_input("sample_input2.txt")
    assert part_two(data) == 281
