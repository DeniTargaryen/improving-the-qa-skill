"""timeit — замерить время вызова, вернуть тот же результат (блок 1.3)."""
import time


def timeit(fn):
    def timed(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        elapsed = time.time() - start
        print(elapsed)
        return result
    return timed