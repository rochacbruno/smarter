import pytest

from smarter import SmartList

given = pytest.mark.parametrize


@given("sl", [SmartList(range(10)), list(range(10))], ids=lambda x: type(x))
def test_slices_like_a_regular_list(sl):
    assert sl[0] == 0
    assert sl[-1] == 9
    assert sl[-2] == 8
    assert sl[1:3] == [1, 2]
    assert sl[:3] == [0, 1, 2]
    assert sl[3:] == [3, 4, 5, 6, 7, 8, 9]
    assert sl[:] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sl[::2] == [0, 2, 4, 6, 8]
    assert sl[::-1] == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert sl[::-2] == [9, 7, 5, 3, 1]
    assert sl[::-3] == [9, 6, 3, 0]
    assert sl[::-4] == [9, 5, 1]
    assert sl[::-5] == [9, 4]


@given("sl", [SmartList(range(10)), list(range(10))], ids=lambda x: type(x))
def test_append_like_a_regular_list(sl):
    sl.append(10)
    assert sl == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sl.append(11)
    assert sl == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


@given("sl", [SmartList(range(10)), list(range(10))], ids=lambda x: type(x))
def test_insert_like_a_regular_list(sl):
    sl.insert(0, 10)
    assert sl == [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sl.insert(1, 11)
    assert sl == [10, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sl.insert(10, 12)
    assert sl == [10, 11, 0, 1, 2, 3, 4, 5, 6, 7, 12, 8, 9]


@given("sl", [SmartList(range(10)), list(range(10))], ids=lambda x: type(x))
def test_pop_like_a_regular_list(sl):
    assert sl.pop() == 9
    assert sl.pop(0) == 0
    assert sl.pop(-1) == 8
    assert sl.pop(1) == 2
    assert sl.pop(1) == 3
    assert sl.pop(1) == 4
    assert sl.pop(1) == 5
    assert sl.pop(1) == 6
    assert sl.pop(1) == 7
    with pytest.raises(IndexError):
        sl.pop(1)


@given("sl", [SmartList(range(10))], ids=lambda x: type(x))
def test_get_item_from_list_by_index(sl):
    assert sl[0] == 0
    assert sl[-1] == 9
    assert sl.get(99, 0) == 0


@given("sl", [SmartList(range(10))], ids=lambda x: type(x))
def test_get_first_item_from_list(sl):
    assert sl.first() == 0


@given("sl", [SmartList(range(10))], ids=lambda x: type(x))
def test_get_last_item_from_list(sl):
    assert sl.last() == 9


@given("sl", [SmartList()], ids=lambda x: type(x))
def test_first_or_default_item_from_list(sl):
    assert sl.first_or(0) == 0


@given("sl", [SmartList()], ids=lambda x: type(x))
def test_last_or_default_item_from_list(sl):
    assert sl.last_or(0) == 0


@given("sl", [SmartList([None, [], "", 13])], ids=lambda x: type(x))
def test_get_first_not_null_from_list(sl):
    assert sl.first_not_null() == []
    assert SmartList().first_not_null(99) == 99


@given("sl", [SmartList([None, [], "", 13])], ids=lambda x: type(x))
def test_first_not_nullable_from_list(sl):
    assert sl.first_not_nullable() == 13
    assert SmartList().first_not_nullable(98) == 98
