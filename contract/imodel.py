from abc import ABC, abstractmethod

from contract.direction import Direction
from contract.square import Square


class IModel(ABC):
    @abstractmethod
    def getFromKey(self, key: str) -> str:
        ...

    @abstractmethod
    def getSquareByXY(self, x: int, y: int) -> Square:
        ...

    @abstractmethod
    def getCharacterXY(self) -> int:
        ...

    @abstractmethod
    def setCharacterXY(self, x: int, y: int):
        ...

    @abstractmethod
    def setCharacterDirection(self, direction: Direction):
        pass

    @abstractmethod
    def moveMobile(self):
        pass
