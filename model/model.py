import random

from contract.direction import Direction
from contract.imodel import IModel
import json

from contract.square import Square
from model.character import Character


class Model(IModel):
    __grid: [[Square]]
    __character: Character

    def __init__(self):
        with open("data/data.json") as jsonfile:
            self.__data = json.load(jsonfile)
        self.__grid = []
        for i in range(self.getFromKey("height")):
            temp = []
            for j in range(self.getFromKey("width")):
                if random.randint(0, 10) == 0:
                    temp.append(Square.WALL)
                else:
                    temp.append(Square.FREE)

            self.__grid.append(temp)
        self.__character = Character(self.getFromKey("startX"),
                                     self.getFromKey("startY"))
        self.__character.setModel(self)

    def getFromKey(self, key: str) -> str:
        try:
            return self.__data[key]
        except KeyError:
            return "Clé " + key + " inconnue"

    def getSquareByXY(self, x: int, y: int) -> Square:
        return self.__grid[y][x]

    def getCharacterXY(self) -> int:
        return self.__character.getX(), self.__character.getY()

    def setCharacterXY(self, x: int, y: int):
        self.__character.setX(x)
        self.__character.setY(y)

    def setCharacterDirection(self, direction: Direction):
        self.__character.setDirection(direction)

    def moveMobile(self):
        self.__character.move()
