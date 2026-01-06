from typing import Callable


def cache(func: Callable) -> Callable:
    result = dict()

    def inner(*args) -> Callable:
        if result.get(args) is None:
            print("Calculating new result")
            result[args] = func(*args)
            return result[args]
        else:
            print("Getting from cache")
            return result[args]
    return inner
