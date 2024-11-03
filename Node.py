class Node:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.has_circle_previous = False
        self.symbol = self.get_symbol()

    def get_symbol(self):
        if self.color == "red":
            return "+"
        elif self.color == "purple":
            return "-"
        elif self.color == "metal":
            return "M"
        elif self.color == "white":
            return "O"
        else:
            return "X"

    def set_cell(self, board):
        if self.is_empty_cell(board):
            board[self.position[0]][self.position[1]] = self

    def is_empty_cell(self, board):
        return board[self.position[0]][self.position[1]].symbol == "X"

    def get_node_at_position(board, position):
        for row in board:
            for node in row:
                if isinstance(node, Node) and node.position == position:
                    return node
        return None
