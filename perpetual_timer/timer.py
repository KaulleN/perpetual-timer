# -*- encoding: utf-8 -*-

import threading
from typing import Callable
from typing import Optional


class PerpetualTimer(threading.Thread):
    def __init__(self, interval: float, function: Callable, initial_interval: Optional[float] = None,
                 args=None, kwargs=None) -> None:
        super().__init__()
        self.setDaemon(True)
        self.interval = interval
        self.function = function
        self.initial_interval = initial_interval
        self.args = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}
        self.finished = threading.Event()

    def cancel(self) -> None:
        """Stop the timer if it hasn't finished yet."""
        self.finished.set()

    def _run(self, interval: float) -> bool:
        self.finished.wait(interval)
        if not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            return True
        return False

    def run(self) -> None:
        if self.initial_interval is not None:
            self._run(self.initial_interval)
        is_running = True
        while is_running:
            is_running = self._run(self.interval)
