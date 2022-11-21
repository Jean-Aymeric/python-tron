class Character:
    __x: int
    __y: int

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def getX(self) -> int:
        return self.__x

    def setX(self, x: int) -> None:
        self.__x = x

    def getY(self) -> int:
        return self.__y

    def setY(self, y: int) -> None:
        self.__y = y

