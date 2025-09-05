def callLimit(limit: int):
    """Decorator to limit the number of times a function can be called."""
    count = 0
    def callLimiter(function):
        """ Limit the number of times a function can be called. """
        def limit_function(*args, **kwds):
            """Limit the number of times a function can be called."""
            nonlocal count
            nonlocal limit
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter