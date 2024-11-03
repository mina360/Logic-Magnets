class Graph:
    def __init__(self):
        self.boards = {}

    def add_board(self, value):
        self.boards[value] = []

    def add_edge(self, from_board, to_board):
        if from_board in self.boards and to_board in self.boards:
            self.boards[from_board].append(to_board)
            self.boards[to_board].append(from_board)

    def get_neighbors(self, board):
        return self.boards[board]