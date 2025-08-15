def ft_filter(function, iterable):
    """
        ft_filter(function or None, iterable) --> ft_filter object

        Return an iterator yielding those items of iterable for which function(item)
        is true. If function is None, return the items that are true.
    """
    try:
        if not function:
            ret = (item for item in iterable)
        else:
            ret = (item for item in iterable if function(item))
    except Exception as error:
        print(f"Error: {error}")
    return ret
