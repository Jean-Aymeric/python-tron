from contract.action import Action
from contract.direction import Direction
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
            self.__model.moveMobile()
            self.__view.showGrid()

    def performAction(self, action: Action):
        newX, newY = self.__model.getCharacterXY()
        if action == Action.CLOSE:
            self.__running = False
        elif action == Action.UP:
            self.__model.setCharacterDirection(Direction.NORTH)
        elif action == Action.DOWN:
            self.__model.setCharacterDirection(Direction.SOUTH)
        elif action == Action.LEFT:
            self.__model.setCharacterDirection(Direction.WEST)
        elif action == Action.RIGHT:
            self.__model.setCharacterDirection(Direction.EAST)
        elif action == Action.STOP:
            self.__model.setCharacterDirection(Direction.MIDDLE)
