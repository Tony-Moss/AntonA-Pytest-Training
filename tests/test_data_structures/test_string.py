import pytest


def test_string_capitalize(string_example):
    capitalize = string_example.capitalize()
    assert capitalize[0] == 'Д'


def test_string_isupper(string_example):
    assert not string_example.isupper()


def test_string_split(string_example):
    assert len(string_example.split()) == 7


def test_string_count(string_example):
    assert string_example.count('а') == 4


@pytest.mark.parametrize('numbers', ['1 2 3 4', '5 6 7 8', '9 10 11 12', '13 14 15 16'])
def test_string_replace(numbers):
    no_space = numbers.replace(' ', '')
    assert no_space.isnumeric()
