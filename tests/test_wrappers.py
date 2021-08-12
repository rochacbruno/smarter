import pytest

from smarter import Result


def this_fails(x):
    return x / 0


def this_succeeds(x):
    return 1 + x


def test_failure():
    w = Result(this_fails, 5)
    assert w.is_error()
    assert w.is_ok() is False
    assert w.exc is not None
    assert isinstance(w.exc, ZeroDivisionError)
    assert "division by zero" in str(w.exc)
    assert w.unwrap_or(5) == 5
    assert w.unwrap_or_else(lambda: 5) == 5
    with pytest.raises(ZeroDivisionError):
        assert w.and_then(lambda x: x + 1, 5) == 6
    with pytest.raises(Exception):
        w.unwrap()


def test_success():
    w = Result(this_succeeds, 5)
    assert w.is_error() is False
    assert w.is_ok()
    assert w.exc is None
    assert w.unwrap_or(5) == 6
    assert w.unwrap_or_else(lambda: 5) == 6
    assert w.and_then(lambda value, x: value * x, 5).unwrap() == 30
    assert w.unwrap() == 6

    def double_integer(x):
        return x * 2

    assert (
        w.and_then(double_integer)  # 12
        .and_then(double_integer)  # 24
        .and_then(double_integer)  # 48
        .and_then(double_integer)  # 96
        .unwrap()
    ) == 96
    assert w.ok() == 6


def test_specific_exceptions():
    person = {"name": "John", "age": "25"}
    w = Result(person.__getitem__, "city", suppress=KeyError)
    w.is_error()
    w.exc
    w.unwrap_or("Gotham")

    # When exception type is specified, other exceptions are not wrapped
    # raising the original exception eagerly/immediately.
    with pytest.raises(TypeError):
        w = Result(person.get, "city", "other", "another", suppress=KeyError)
