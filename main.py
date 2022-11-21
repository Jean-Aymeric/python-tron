from controller.controller import Controller
from model.model import Model
from view.viewTkinter import ViewTkinter
from view.view import View

controller = Controller(ViewTkinter(), Model())
controller.start()
