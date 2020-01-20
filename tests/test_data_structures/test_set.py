import pytest


@pytest.fixture()
def set_days1():
    return {'sunday', 'monday', 'tuesday', 'sunday'}


@pytest.fixture()
def set_days2():
    return {'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}


@pytest.fixture()
def set_word1():
    return set('полупроводник')


def test_set_duplicates(set_days1):
    assert len(set_days1) == 3


def test_set_createset(set_word1):
    assert set_word1 == {'у', 'р', 'и', 'п', 'о', 'л', 'д', 'н', 'в', 'к'}


def test_set_letter(set_word1):
    print(set_word1)
    assert 'о' in set_word1


def test_set_union(set_days1, set_days2):
    assert len(set_days1.union(set_days2)) == 7


@pytest.mark.parametrize('param1',
                         [set('monday'), set('tuesday'), set('wednesday'), set('thursday')])
def test_set_common(param1):
    assert param1 & set('day') == {'d', 'a', 'y'}
