from abc import ABC, abstractmethod

from contract.action import Action
from contract.imodel import IModel
from contract.iview import IView


class IController(ABC):
    @abstractmethod
    def getView(self) -> IView:
        ...

    @abstractmethod
    def getModel(self) -> IModel:
        ...

    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def performAction(self, action: Action):
        ...
