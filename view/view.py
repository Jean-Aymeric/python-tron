from contract.imodel import IModel
from contract.iview import IView


class View(IView):
    __model: IModel

    def display(self, message) -> None:
        print(message)

    def setModel(self, model: IModel):
        self.__model = model
