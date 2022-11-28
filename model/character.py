from model.mobile import Mobile


class Character(Mobile):
    def __init__(self, x: int, y: int):
        Mobile.__init__(self, x, y)
