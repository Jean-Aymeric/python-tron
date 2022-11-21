import random
from time import sleep

from contract.action import Action
from contract.icontroller import IController
from contract.imodel import IModel
from contract.iview import IView


class Controller(IController):
    __view: IView
    __model: IModel
    __running: bool

    def __init__(self, view: IView, model: IModel):
        self.__view = view
        self.__model = model
        self.__view.setModel(self.__model)
        self.__view.setController(self)
        self.__running = True

    def getView(self) -> IView:
        return self.__view

    def getModel(self) -> IModel:
        return self.__model

    def start(self):
        self.__view.showGrid()
        self.__gameLoop()

    def __gameLoop(self):
        while self.__running:
            self.__view.showGrid()

    def performAction(self, action: Action):
        newX, newY = self.__model.getCharacterXY()
        if action == Action.CLOSE:
            self.__running = False
        elif action == Action.UP:
            newY = (newY - 1 + self.__model.getFromKey("height")) % self.__model.getFromKey("height")
        elif action == Action.DOWN:
            newY = (newY + 1 + self.__model.getFromKey("height")) % self.__model.getFromKey("height")
        elif action == Action.LEFT:
            newX = (newX - 1 + self.__model.getFromKey("width")) % self.__model.getFromKey("width")
        elif action == Action.RIGHT:
            newX = (newX + 1 + self.__model.getFromKey("width")) % self.__model.getFromKey("width")
        self.__model.setCharacterXY(newX, newY)
