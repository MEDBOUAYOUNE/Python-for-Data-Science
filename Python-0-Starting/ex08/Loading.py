def ft_tqdm(lst: range) -> None:
    """
        Decorate an iterable object, returning an iterator which acts exactly
        like the original iterable, but prints a dynamically updating
        progressbar every time a value is requested.
    """
    total = len(lst)
    for i, item in enumerate(lst, start=1):
        bar = "█" * ((i * 100) // total)
        print(f"\r{(i * 100) // total}%|{bar:<100}| {i}/{total}", end="")
        yield item
