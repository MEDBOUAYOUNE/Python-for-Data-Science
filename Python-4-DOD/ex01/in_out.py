from __future__ import annotations

def square(x: int | float) -> int | float:
    """Return the square of a number."""
    return x * x

def pow(x: int | float) -> int | float:
    """Return the power of a number."""
    return x ** x

def outer(x: int | float, function) -> object:
    """Return a closure that applies the given function to x."""
    def inner() -> int | float:
        """Return the result of applying the function to x."""
        nonlocal x
        x = function(x)
        return x
    return inner