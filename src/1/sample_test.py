import pytest
import os
from main import part_one, part_two

@pytest.fixture
def sample_input() -> str:
    input_path = os.path.join(os.path.dirname(__file__), "input/sample_input.txt")
    with open(input_path) as file:
        return file.read()

def test_part_one(sample_input: str):
    assert part_one(sample_input) is None

def test_part_two(sample_input: str):
    assert part_two(sample_input) is None
