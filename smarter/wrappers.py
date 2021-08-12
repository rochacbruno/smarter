failure = object()


class Result:
    """
    Wraps a callable and calls it with the given arguments
    if an exception is raised in the callable, it is wrapped.
    """

    def __init__(self, _callable, *args, suppress=Exception, **kwargs):
        """
        >>> w = Result(lambda x: x, 1)
        >>> w.unwrap()
        1
        >>> w = Result(lambda x: x, 1, suppress=TypeError)
        >>> w.unwrap()
        1
        >>> w = Result(lambda x, y: x, 1)
        >>> w.unwrap()
        Traceback (most recent call last):
        ...
        TypeError: missing required positional argument: 'y'
        >>> w = Result(lambda x, y: x, 1)
        >>> w.unwrap_or("default")
        'default'
        >>> w.unwrap_or_else(lambda: "default")
        'default'
        >>> w.is_ok()
        False
        >>> w.is_error()
        True
        >>> w = Result(lambda: 2)
        >>> w.and_then(lambda value, x: x * value, 5)
        10
        """
        self.exc = None
        self.value = failure
        try:
            self.value = _callable(*args, **kwargs)
        except suppress as e:
            self.exc = e

    def unwrap(self):
        """
        If an exception was raised in the wrapped callable,
        raise it otherwise return the result value.
        """
        if self.exc is not None:
            raise self.exc
        return self.value

    def unwrap_or(self, default):
        """
        If an exception was raised in the wrapped callable,
        return the default value otherwise return the result value.
        """
        return self.value if self.value is not failure else default

    def unwrap_or_else(self, _callable, *args, **kwargs):
        """
        If an exception was raised in the wrapped callable,
        return the result of passed calleble otherwise return the result value.
        """
        return self.unwrap_or(_callable(*args, **kwargs))

    def is_ok(self):
        """
        Tells if the wrapped callable returned without error.
        """
        return self.value is not failure

    def is_error(self):
        """
        Tells if the wrapped callable raised an exception.
        """
        return self.value is failure

    def ok(self):
        """
        Same as unwrap().
        """
        return self.unwrap()

    def and_then(self, _callable, *args, **kwargs):
        """
        If no exception was raised in the wrapped callable,
        pass the result value to the given callable.
        as a wrapped callable.
        """
        return Result(_callable, self.unwrap(), *args, **kwargs)
