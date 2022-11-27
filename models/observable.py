from typing import Callable


class Observable:
    def __init__(self, initialValue=None):
        self.data = initialValue
        self.callbacks = {}

    def addCallback(self, func: Callable):
        self.callbacks[func] = 1

    def addMultipleCallback(self, funcs: list[Callable]):
        for func in funcs:
            self.callbacks[func] = 1

    def delCallback(self, func: Callable):
        del self.callbacks[func]

    def _docallbacks(self):
        for func in self.callbacks:
            func(self.data)

    def set(self, data):
        self.data = data
        self._docallbacks()

    def get(self):
        return self.data

    def unset(self):
        self.data = None
