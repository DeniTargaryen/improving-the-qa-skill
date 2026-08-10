"""Timer — context manager с elapsed (блок 1.3)."""
import time


class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.end = time.time()
        self.elapsed = self.end - self.start
