class Cell:
    def __init__(self, color, position=[]):
        self.color = color
        self.symbol = self.initSymbol()
        self.position = position
        self.neighbors = []
        self.has_prev_circle = False

    def initSymbol(self):
        if self.color == "red":
            return "+"
        elif self.color == "purple":
            return "-"
        elif self.color == "metal":
            return "M"
        elif self.color == "white":
            return "O"
        else:
            self.color = 'empty'
            return "X"

    def setPosition(self, position):
        self.position = position
        return self

    def setColor(self, color):
        self.color = color
        if self.color == "red":
            self.symbol = "+"
        elif self.color == "purple":
            self.symbol = "-"
        elif self.color == "metal":
            self.symbol = "M"
        elif self.color == "white":
            self.symbol = "O"
        else:
            self.color = 'empty'
            self.symbol = "X"
        return self

    def isEmpty(self):
        return self.symbol == "X"
