import logging
import time
from contextlib import contextmanager

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

class Metrics:
    def __init__(self):
        self.data = {}

    def record(self, name: str, value: float):
        self.data[name] = value

    def export(self):
        return self.data


@contextmanager
def trace(task_name: str):
    start = time.time()
    logging.info(f"START task={task_name}")
    yield
    duration = time.time() - start
    logging.info(f"END task={task_name} duration={duration:.2f}s")
