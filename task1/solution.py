import inspect
from functools import wraps


def strict(func):
    sig = inspect.signature(func)
    ann = func.__annotations__

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            expected_type = ann.get(name)
            if expected_type is None:
                continue
            if type(value) is not expected_type:
                raise TypeError(
                    f"Argument '{name}' must be {expected_type.__name__}, "
                    f"got {type(value).__name__}"
                )
        return func(*args, **kwargs)

    return wrapper
