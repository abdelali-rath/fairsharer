import pytest
from main import fair_sharer


# Unit-test
def test_fair_sharer():
    

    # 1 - Examples like the ones in main.py
    values = [0, 1000, 800, 0]
    assert fair_sharer(values, 1) == [100, 800, 900, 0], "Test 1.1 failed"
    assert fair_sharer(values, 2) == [100, 890, 720, 90], "Test 1.2 failed"

    # 2 - same numbers everywherer
    values = [10, 10, 10]
    assert fair_sharer(values, 1) == [10, 10, 10], "Test 2 failed"

    # 3- Neighbors
    values = [10, 0, 0, 10]
    assert fair_sharer(values, 1) == [8, 1, 0, 11], "Test 3 failed"

    # 4 - negative numbers
    values = [-100, 200, -50, 50]
    assert fair_sharer(values, 1) == [-80, 160, -30, 50], "Test 4 faield"

    # 5 - 0 iterations
    values = [100, 200, 300]
    assert fair_sharer(values, 0) == [100, 200, 300], "Test 5 failed"


if __name__ == "__main__":
    pytest.main()
