import pytest


def test_list_append(list_letters):
    list_letters.append('f')
    assert list_letters == ['a', 'b', 'c', 'd', 'e', 'f']


def test_list_clear(list_letters):
    list_letters.clear()
    assert list_letters == []


def test_list_reverse(list_letters):
    list_letters.reverse()
    assert list_letters == ['e', 'd', 'c', 'b', 'a']


def test_list_index(list_letters):
    assert list_letters.pop(3) == 'd'


@pytest.mark.parametrize("param1", [[0, 1, 2], [65, 99, 1, 7, 7, 23]])
@pytest.mark.parametrize("param2", [[1, 8, 2], [-234, 9, 656456456, 1]])
def test_list_count(param1, param2):
    combined = param1 + param2
    assert combined.count(1) == 2
