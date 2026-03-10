###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


from collections import defaultdict
from typing import Callable, Any


class EventManager:

    def __init__(self) -> None:
        self._listeners: dict[str, list[Callable]] = defaultdict(list)
        self._queue: list[tuple[str, Any]] = []

    def subscribe(self, event: str, listener: Callable) -> None:
        if not isinstance(event, str): raise TypeError()
        if not callable(listener): raise TypeError()
        self._listeners[event].append(listener)

    def unsubscribe(self, event: str, listener: Callable) -> None:
        if event in self._listeners:
            if listener in self._listeners[event]:
                self._listeners[event].remove(listener)

    def emit(self, event: str, data: Any = None) -> None:
        if event not in self._listeners:
            return
        for listener in list(self._listeners[event]):
            listener(data)

    def queue(self, event: str, data: Any = None) -> None:
        self._queue.append((event, data))

    def process(self) -> None:
        while self._queue:
            event, data = self._queue.pop(0)
            self.emit(event, data)

    def clear(self) -> None:
        self._listeners.clear()
        self._queue.clear()

    def __repr__(self) -> str:
        return (
            f"<EventManager listeners={len(self._listeners)} "
            f"queued={len(self._queue)}>"
        )
