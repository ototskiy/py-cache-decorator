from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = dict()

    def inner(*args) -> Any:
        if not args in result:
            print("Calculating new result")
            result[args] = func(*args)
            return result[args]
        else:
            print("Getting from cache")
            return result[args]
    return inner
