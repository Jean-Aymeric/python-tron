from contract.imodel import IModel
from contract.iview import IView
from tkinter import Tk, messagebox, Canvas

from contract.square import Square


class ViewTkinter(IView):
    __model: IModel
    __window: Tk
    __canvas: Canvas

    def __init__(self):
        self.__window = None

    def __createWindow(self):
        self.__window = Tk()
        self.__window.title(self.__model.getFromKey("title"))
        self.__window.geometry(str(self.__model.getFromKey("width") * self.__model.getFromKey("zoom"))
                               + "x"
                               + str(self.__model.getFromKey("height") * self.__model.getFromKey("zoom")))
        self.__canvas = Canvas(self.__window, bg=self.__model.getFromKey("background"))
        self.__canvas.pack(fill="both", expand=True)

    def display(self, message) -> None:
        messagebox.showinfo(self.__model.getFromKey("title"), message)

    def setModel(self, model: IModel):
        self.__model = model

    def askYesNo(self, message: str) -> bool:
        return messagebox.askyesno(self.__model.getFromKey("title"), message)

    def showGrid(self):
        if self.__window is None:
            self.__createWindow()
            zoom = self.__model.getFromKey("zoom")
            for y in range(self.__model.getFromKey("height")):
                for x in range(self.__model.getFromKey("width")):
                    if self.__model.getSquareByXY(x, y) == Square.FREE:
                        self.__canvas.create_rectangle(x*zoom,
                                                       y*zoom,
                                                       (x+1)*zoom,
                                                       (y+1)*zoom,
                                                       outline=self.__model.getFromKey("color"))
        self.__window.update()
