import pytest


def test_dict_add(dict_age):
    dict_age['Gordon'] = 40
    assert len(dict_age) == 4


def test_dict_sortvalues(dict_age):
    ages = sorted(dict_age.values())
    assert ages[0] == 11


def test_dict_delete(dict_age):
    del dict_age['Arthur']
    assert dict_age == {'Michael': 31, 'Jack': 11}


def test_dict_update(dict_age):
    new_ages = dict(Mary=20, Albert=56)
    dict_age.update(new_ages)
    assert len(dict_age) == 5


@pytest.mark.parametrize('names', ['Arthur', 'Jack', 'Michael'])
def test_dict_contain(dict_age, names):
    assert names in dict_age
