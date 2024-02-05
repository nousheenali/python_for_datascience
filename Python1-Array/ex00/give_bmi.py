import numpy as np


def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    try:
        # performs element-wise division
        bmi = np.array(weight) / np.array(height) ** 2
        return bmi.tolist()
    except TypeError:
        print(TypeError.__name__ + ":", "list values should be int or float")
        exit(1)
    except Exception as e:
        print(type(e).__name__ + ":", e)
        exit(1)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        return (np.array(bmi) > limit).tolist()
    except TypeError:
        print(TypeError.__name__ + ":", "list values should be int or float")
        exit(1)
    except Exception as e:
        print(type(e).__name__ + ":", e)
        exit(1)

# Alternate solution:
# def give_bmi(
#         height: list[int | float], weight: list[int | float]
#         ) -> list[int | float]:
#     """
#     This function calculates the BMI of a person based on their height and
#     weight.
#     Arguments:  two lists, one for height and one for weight.
#     Return: List of BMI values.
#     bmi calculation = weight / height ** 2
#     """
#     try:
#         # zip is a built-in Python function that allows you to iterate over
#         # multiple iterables (e.g., lists, tuples) in parallel
#         ouptut = [w / h ** 2 for w, h in zip(weight, height)]
#         return ouptut
#     except TypeError:
#         print(TypeError.__name__ + ":", "list values should be int or float")
#     except Exception as e:
#         print(type(e).__name__ + ":", e)


# def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
#     """
#     This function takes a list of BMI values and a limit and returns a list
#     of booleans indicating whether each corresponding BMI value is above the
#     limit.
#     Arguments:   lists of BMI values and a limit.
#     return: List of booleans.
#     """
#     try:
#         outut = [True if x > limit else False for x in bmi]
#         return outut
#     except TypeError:
#         print(TypeError.__name__ + ":", "values provided not int or float")
#     except Exception as e:
#         print(type(e).__name__ + ":", e)


# '''
# With square brackets (list comprehension):
# ------------------------------------------
# bmi_values = [w / h ** 2 for h, w in zip(height, weight)]
# This creates a list and stores all BMI values in memory.
# You can access any element of bmi_values directly, and it consumes memory.

# With normal parentheses (generator expression):
# ----------------------------------------------
# bmi_values_generator = (w / h ** 2 for h, w in zip(height, weight))
# This creates a generator object that generates BMI values on-the-fly when
# iterated over. It doesn't store the entire list of values in memory.
# You can iterate over bmi_values_generator in a loop or convert it to a list
# using list(bmi_values_generator) if you want to store the values in memory.

# use a list comprehension if you need to access the elements multiple times or
# need random access to the elements. Use a generator expression if you are
# working with large datasets and want to save memory by generating values
# on-the-fly during iteration.
# '''
