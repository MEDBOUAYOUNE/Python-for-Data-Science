def mean(*args):
    """ """
    data = args
    print(f"mean : {float(sum(data)/len(data))}")


def median(*args):
    """ """
    data = args
    data = sorted(data)
    print(f"median : {data[len(data) // 2]}")


def quartile(*args):
    """ """
    data = sorted(args)
    q1 = data[len(data) // 4]
    q3 = data[(len(data) * 3) // 4]
    print(f"quartile : {[q1, q3]}")


def var(*args):
    """ """
    data = args
    mean_value = sum(data) / len(data)
    variance = sum((x - mean_value) ** 2 for x in data) / len(data)
    print(f"var : {variance}")


def std(*args):
    """ """
    data = args
    mean_value = sum(data) / len(data)
    variance = sum((x - mean_value) ** 2 for x in data) / len(data)
    std_deviation = variance ** 0.5
    print(f"std : {std_deviation}")


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Compute and print various statistics based on provided data and requested metrics.
    """
    if not args and not kwargs:
        return 
    if not args:
        print("ERROR")
        return
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
