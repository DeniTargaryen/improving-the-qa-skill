"""retry — повторить вызов при исключении (блок 1.3)."""


def retry(times=3):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            err = None
            for _ in range(times):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    err = e
            raise err

        return wrapper

    return decorator
