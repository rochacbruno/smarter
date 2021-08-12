import pytest

from smarter import SmartList, get

given = pytest.mark.parametrize


def test_get_from_a_dict():
    """
    Test get from a dictionary
    """
    d = {"a": 1, "b": 2}
    assert d >> get("a") == 1
    assert d >> get("b") == 2
    assert d >> get("c") is None


@given(
    "nums", [SmartList([1, 2, 3]), [1, 2, 3], (1, 2, 3)], ids=lambda x: type(x)
)
def test_get_from_a_list(nums):
    """
    Test get from a list
    """
    assert nums >> get(0) == 1
    assert nums >> get(1) == 2
    assert nums >> get(2) == 3
    assert nums >> get(3) is None


def test_custom_obj_get():
    class Custom:
        def get(self, item, default=None):
            return (default or item).upper()

    custom = Custom()
    assert custom >> get("a") == "A"
    assert custom >> get("a", "b") == "B"


def test_custom_obj_getitem():
    class Custom:
        def __getitem__(self, item):
            if item == "notexist":
                raise KeyError
            return item.upper()

    custom = Custom()
    assert custom >> get("a") == "A"
    assert custom >> get("b", "ignored") == "B"
    assert custom >> get("notexist", "C") == "C"


def test_custom_obj_getattr():
    class Custom:
        @property
        def bazinga(self):
            return "Bazinga!"

    custom = Custom()
    assert custom >> get("bazinga") == "Bazinga!"
    assert custom >> get("notexist") is None
