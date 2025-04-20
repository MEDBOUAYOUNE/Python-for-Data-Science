#Ref : https://tqdm.github.io/
#Range : returns a sequence of elements(intgers)
#enumerate: useful function for iterating into sequences.

def ft_tqdm(lst: range) -> None:
    total = len(lst)

    for i, item in enumerate(lst, start=1):
        bar = "█" * ((i * 100) // total)
        print(f"\r{(i * 100) // total}%|{bar:<50}| {i}/{total}", end="")

        yield item
        
    
