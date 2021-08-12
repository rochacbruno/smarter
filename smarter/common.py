# borrowed from: dhilst/geckones_twitter_bots/blob/master/utils.py
import contextlib
from typing import Mapping, Sequence


class get:  # noqa
    """
    This will emulate .get method for

    dicts, lists and tuples

    You can use like this
    >>> [1] >> get(2, 'Not found')
    'Not found'
    >>> [1] >> get(2)
    >>> [1] >> get(0)
    1
    >>> {} >> get('a', 'Not found')
    >>> () >> get(0, 'Not found')
    """

    def __init__(self, item, default=None):
        self.item = item
        self.default = default

    def __rrshift__(self, other):
        other_type = get_base_type(other)
        return getattr(self, f"_get_{other_type}", self._get)(other)

    def _get(self, other):
        if hasattr(other, "get"):
            return other.get(self.item, self.default)
        elif hasattr(other, "__getitem__"):
            with contextlib.suppress(KeyError):
                return other[self.item]
            return self.default
        return getattr(other, self.item, self.default)

    def _get_sequence(self, other):
        with contextlib.suppress(IndexError):
            return other[self.item]
        return self.default

    def _get_mapping(self, other):
        return other.get(self.item, self.default)


def get_base_type(other):
    """
    >>> get_base_type(1)
    int
    >>> get_base_type([])
    sequence
    >>> get_base_type({})
    mapping
    """
    if isinstance(other, Mapping):
        return "mapping"
    if isinstance(other, Sequence):
        return "sequence"
    return type(other).__name__.lower()
