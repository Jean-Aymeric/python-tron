import tkinter
from time import sleep

from contract.action import Action
from contract.icontroller import IController
from contract.imodel import IModel
from contract.iview import IView
from tkinter import Tk, messagebox, Canvas, NW
from PIL import Image, ImageTk
from contract.square import Square


class ViewTkinter(IView):
    __model: IModel
    __controller: IController
    __window: Tk
    __canvas: Canvas
    __character: Canvas

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
        self.__window.protocol("WM_DELETE_WINDOW", self.__onClosing)
        self.__window.bind("<Key>", self.__manageKeyboard)

    def __manageKeyboard(self, event: tkinter.Event):
        if event.keysym == "Up":
            self.__controller.performAction(Action.UP)
        elif event.keysym == "Down":
            self.__controller.performAction(Action.DOWN)
        elif event.keysym == "Left":
            self.__controller.performAction(Action.LEFT)
        elif event.keysym == "Right":
            self.__controller.performAction(Action.RIGHT)

    def __onClosing(self):
        self.__controller.performAction(Action.CLOSE)

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
            xCharacter, yCharacter = self.__model.getCharacterXY()
            # image = ImageTk.PhotoImage(Image.open("JADT.jpg"))
            # self.__character = self.__canvas.create_image(xCharacter*zoom,
            #                                               yCharacter*zoom,
            #                                               anchor=NW, image=image)
            self.__character = self.__canvas.create_oval(xCharacter*zoom,
                                                         yCharacter*zoom,
                                                         (xCharacter+1) * zoom,
                                                         (yCharacter+1) * zoom,
                                                         outline=self.__model.getFromKey("color"),
                                                         fill="red")
        else:
            xCharacter, yCharacter = self.__model.getCharacterXY()
            zoom = self.__model.getFromKey("zoom")
            for i in range(zoom//2):
                newX = self.__canvas.coords(self.__character)[0]
                newY = self.__canvas.coords(self.__character)[1]
                if newX != (xCharacter * zoom):
                    newX += 2*((newX > (xCharacter * zoom)) * (-1) + (newX < (xCharacter * zoom)))
                if newY != (yCharacter * zoom):
                    newY += 2*((newY > (yCharacter * zoom)) * (-1) + (newY < (yCharacter * zoom)))
                self.__canvas.coords(self.__character, newX, newY, (newX+zoom), (newY+zoom))
                self.__window.update()
                sleep(0.01)
        self.__window.update()
    def setController(self, controller) -> None:
        self.__controller = controller
