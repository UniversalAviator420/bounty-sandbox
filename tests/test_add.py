from scripts.add import add


def test_add_returns_sum():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
