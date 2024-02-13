def ft_mean(*args: any) -> float:
    """
    This function returns the mean of the given numbers.
    mean = sum of all numbers / total numbers
    """
    sum = 0.0
    for i in args:
        sum += i
    return (sum / len(args))


def ft_sort(*args: any) -> list:
    """
    This function sorts the given numbers in ascending order.
    """
    new_args = list(args)
    for i in range(len(new_args)):
        for j in range(len(new_args) - 1):
            if new_args[j] > new_args[j + 1]:
                new_args[j], new_args[j + 1] = new_args[j + 1], new_args[j]
    return new_args


def ft_median(*args: any) -> float:
    """
    This function returns the median of the given numbers.
    * If the number of elements is odd, the median is the middle element.
    * If the number of elements is even, the median is the average of the
    two middle elements.
    """
    new_args = list(ft_sort(*args))
    n = len(new_args)
    # // is used for floor division
    if n % 2 == 0:
        return ((new_args[n // 2 - 1] + new_args[n // 2]) / 2)
    else:
        return (new_args[n // 2])


def ft_quartile(*args: any) -> tuple[float, float]:
    """
    This function returns the first and third quartile of the given numbers.
    """
    new_args = ft_sort(*args)
    n = len(new_args)
    # check if n * (1 / 4) is an integer
    if (n * (1 / 4)).is_integer():
        Q1 = ft_mean(new_args[int(n * 1 / 4) - 1], new_args[int(n * 1 / 4)])
        Q3 = ft_mean(new_args[int(n * 3 / 4) - 1], new_args[int(n * 3 / 4)])
    else:
        Q1 = new_args[int(n * (1 / 4))]
        Q3 = new_args[int(n * (3 / 4))]
    return (Q1, Q3)


def ft_var(*args: any) -> float:
    """
    Returns the variance of the given numbers.
    Variance is a measure of how much values in
    a data set differ from the mean.
    Formula:
    variance = sum of (x - mean) ** 2 / total numbers
    """
    mean = ft_mean(*args)
    sum = 0.0
    for i in args:
        sum += (i - mean) ** 2
    return (sum / len(args))


def std_dev(*args: any) -> float:
    """
    Returns the standard deviation of the given numbers.
    Standard deviation is a measure of the amount of variation
    or dispersion of a set of values.
    Formula:
    standard deviation = sqrt(variance)
    """
    var = ft_var(*args)
    return (var ** 0.5)  # sqrt(variance)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    This function returns the mean, median, quartile,
    variance, and standard deviation of the given numbers.
    """
    func_dict = {'mean': ft_mean,
                 'median': ft_median,
                 'quartile': ft_quartile,
                 'std': std_dev,
                 'var': ft_var}
    for key, value in kwargs.items():
        if value in func_dict:
            if len(args) > 0:
                result = func_dict[value](*args)
                print(f"{value} : {result}")
            else:
                print("ERROR")
        else:
            pass


"""
NOTE1:
    *args and **kwargs in Python
    https://www.geeksforgeeks.org/args-kwargs-python/

NOTE2:
    How to calculate the 1st and 3rd quartiles?
    Find the first quartile:
    - Calculate n * (1 / 4).
    - If n * (1 / 4) is an integer, then the first quartile
        is the mean of the numbers at positions n * (1 / 4) and n * (1 / 4)+1
    - If n * (1 / 4) is not an integer, then round it up. The
      number at this position is the first quartile.
    Find the third quartile:
    - Calculate n * (3 / 4).
    - If n * (3 / 4) is an integer, then the third quartile
      is the mean of the numbers at positions n * (3 / 4) and n * (3 / 4) + 1.
    - If n * (3 / 4) is not an integer, then round it up.
    The number at this position is the third quartile.
    https://www.scribbr.com/statistics/quartiles-quantiles/#:~:text=What%20are%20quartiles%3F,falls%20below%20the%20second%20quartile.
"""
