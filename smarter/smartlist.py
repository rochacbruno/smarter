from collections import UserList
from typing import Any, Optional


class SmartList(UserList):
    """
    A list with more utility methods added.
    """

    def get(self, index: int, default: Optional[Any] = None) -> Any:
        """
        Return the element at index or default if index is out of range.
        """
        try:
            return self[index]
        except IndexError:
            return default

    def first(self):
        """
        Return first item of the list
        """
        return self[0]

    def last(self):
        """
        Return last item of the list
        """
        return self[-1]

    def first_or(self, default: Any = None):
        """
        Return first item of the list or default if the list is empty.
        """
        return self.get(0, default)

    def last_or(self, default: Any = None):
        """
        Return last item of the list or default if the list is empty.
        """
        return self.get(-1, default)

    def first_not_null(self, default: Optional[Any] = None) -> Any:
        """
        Return the first non-null item of the list or default.
        """
        for item in self:
            if item is not None:
                return item
        return default

    def first_not_nullable(self, default: Optional[Any] = None):
        """
        Return the first non-nullable item of the list or default.
        """
        for item in self:
            if item:
                return item
        return default
