from abc import ABC, abstractmethod

from contract.square import Square


class IModel(ABC):
    @abstractmethod
    def getFromKey(self, key: str) -> str:
        ...

    @abstractmethod
    def getSquareByXY(self, x: int, y: int) -> Square:
        ...
