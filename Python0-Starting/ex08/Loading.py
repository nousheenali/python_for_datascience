def ft_tqdm(lst: range) -> None:
    """A tqdm-like function that takes a range and
    prints a progress bar to the terminal.
    Args: lst (range): a range of numbers
    Returns: None"""
    total = len(lst)
    progress = 0
    for i in lst:
        progress += 1
        percent = progress / total * 100
        # Adjust the width of the progress bar to match actual tqdm
        barW = 119 # width of the entire progress bar
        fillW = int(percent * barW / 100)  # filled width of the bar
        print(f"\r{percent:.0f}%|[{'='*fillW}>{' '*(barW-fillW)}]| "
              f"{progress}/{total}", end="")
        yield i

# \r is used to move the cursor back to the beginning of the line before
# printing the updated progress information.
