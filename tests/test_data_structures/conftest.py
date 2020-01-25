import pytest


@pytest.fixture()
def list_letters():
    return ['a', 'b', 'c', 'd', 'e']


@pytest.fixture()
def dict_age():
    return {'Arthur': 23, 'Michael': 31, 'Jack': 11}


@pytest.fixture()
def string_example():
    return 'достаточно длинная строка, чтобы можно было разгуляться'
