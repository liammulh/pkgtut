from src.example_package_liammulh.example import add_one


def test_add_one():
    expected = 2
    actual = add_one(1)
    assert actual == expected
