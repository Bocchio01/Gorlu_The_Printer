from abc import ABC, abstractmethod


class ViewABC(ABC):

    @abstractmethod
    def __init__(self) -> None:
        pass
