def mean(*args):
    """
    Print the mean (average) of the given numbers.
    param args: the numbers to process.
    """
    data = args
    print(f"mean : {float(sum(data)/len(data))}")


def median(*args):
    """
    Print the median (middle value) of the given numbers.
    param args: the numbers to process.
    """
    data = sorted(args)
    print(f"median : {data[len(data) // 2]}")


def quartile(*args):
    """
    Print the first (25%) and third (75%) quartiles of the given numbers.
    param args: the numbers to process.
    """
    data = sorted(args)
    q1 = data[len(data) // 4]
    q3 = data[(len(data) * 3) // 4]
    print(f"quartile : {[q1, q3]}")


def var(*args):
    """
    Print the (population) variance of the given numbers.
    param args: the numbers to process.
    """
    data = args
    mean_value = sum(data) / len(data)
    variance = sum((x - mean_value) ** 2 for x in data) / len(data)
    print(f"var : {variance}")


def std(*args):
    """
    Print the (population) standard deviation of the given numbers.
    param args: the numbers to process.
    """
    data = args
    mean_value = sum(data) / len(data)
    variance = sum((x - mean_value) ** 2 for x in data) / len(data)
    std_deviation = variance ** 0.5
    print(f"std : {std_deviation}")


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Compute and print various statistics 
    based on provided data and requested metrics.
    param args: the numbers to process.
    param kwargs: the requested metrics; each value is one of
        "mean", "median", "quartile", "var" or "std".
        Any other value prints ERROR.
    """
    if not args and not kwargs:
        return None
    if not args:
        print("ERROR")
        return None
    for key, value in kwargs.items():
        if value == "mean":
            mean(*args)
        elif value == "median":
            median(*args)
        elif value == "quartile":
            quartile(*args)
        elif value == "var":
            var(*args)
        elif value == "std":
            std(*args)
        else:
            print("ERROR")
