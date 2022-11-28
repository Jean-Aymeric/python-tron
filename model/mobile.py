from abc import ABC

from contract.direction import Direction
from contract.imodel import IModel


class Mobile(ABC):
    __model: IModel
    __x: int
    __y: int
    __direction: Direction

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self.__direction = Direction.NORTH

    def getX(self) -> int:
        return self.__x

    def setX(self, x: int) -> None:
        self.__x = x

    def getY(self) -> int:
        return self.__y

    def setY(self, y: int) -> None:
        self.__y = y

    def getDirection(self) -> Direction:
        return self.__direction

    def setDirection(self, direction: Direction) -> None:
        self.__direction = direction
        print(self.__direction)

    def move(self) -> None:
        newX = self.getX()
        newY = self.getY()
        if self.__direction == Direction.NORTH:
            newY = (newY - 1 + int(self.__model.getFromKey("height"))) % int(self.__model.getFromKey("height"))
        elif self.__direction == Direction.SOUTH:
            newY = (newY + 1 + int(self.__model.getFromKey("height"))) % int(self.__model.getFromKey("height"))
        elif self.__direction == Direction.EAST:
            newX = (newX + 1 + int(self.__model.getFromKey("width"))) % int(self.__model.getFromKey("width"))
        elif self.__direction == Direction.WEST:
            newX = (newX - 1 + int(self.__model.getFromKey("width"))) % int(self.__model.getFromKey("width"))
        self.__model.setCharacterXY(newX, newY)

    def setModel(self, model: IModel):
        self.__model = model
