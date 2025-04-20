#Ref: https://www.shiksha.com/online-courses/articles/python-filter-everything-you-need-to-know/#:~:text=The%20Python%20filter()%20function%20is%20a%20built%2Din%20function,which%20the%20function%20returns%20True.
# print(filter.__doc__)


def ft_filter(function, iterable):
    """ ft_filter(function or None, iterable) --> ft_filter object

        Return an iterator yielding those items of iterable for which function(item)
        is true. If function is None, return the items that are true.
    """
    if function is None:
        return iterable
    
    for item in iterable:
        if function(item):
            yield item
    # new_iterable = [item for item in iterable if function(item)]
    # return new_iterable


def is_even(num):
    return num % 2 == 0

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = ft_filter(is_even, numbers)
    result = list(even_numbers)
    print(result)

     