from Cell import Cell


class Board:
    def __init__(self, size):
        self.size = size
        self.cells = [[Cell('empty', [row, col])
                       for col in range(size)] for row in range(size)]
        self.O_positions = []

    def setCell(self, row, col, color):
        cell = Cell(color, [row, col])
        self.cells[row][col] = cell
        if cell.symbol == "O" and [row, col] not in self.O_positions:
            self.O_positions.append([row, col])
        return cell

    def getCell(self, row, col):
        return self.cells[row][col]

    def findRedCell(self):
        for r in range(len(self.cells)):
            for c in range(len(self.cells[r])):
                if self.cells[r][c].symbol == '+':
                    return self.cells[r][c]

    def findPurpleCell(self):
        for r in range(len(self.cells)):
            for c in range(len(self.cells[r])):
                if self.cells[r][c].symbol == '-':
                    return self.cells[r][c]

    def getCellRowAndColumn(self, cell: Cell):
        cell_row = cell.position[0]
        cell_col = cell.position[1]
        col = []
        for i in range(self.size):
            col.append(self.cells[i][cell_col])
        return self.cells[cell_row], col

    def removeCell(self, row, col):
        self.cells[row][col] = Cell('empty', [row, col])

    def moveCell(self, cell, new_row, new_col):
        old_row, old_col = cell.position
        target_cell = self.cells[new_row][new_col]
        if self.cells[new_row][new_col].symbol not in ['X', 'O']:
            return self
        if cell.has_prev_circle:
            self.cells[old_row][old_col] = Cell('white', [old_row, old_col])
        self.cells[new_row][new_col] = cell
        self.cells[old_row][old_col] = Cell('empty', [old_row, old_col])
        cell.setPosition([new_row, new_col])
        if target_cell.symbol == 'O':
            cell.has_prev_circle = True
        else:
            cell.has_prev_circle = False
        return self

    def printBoard(self):
        board = [["X" for _ in range(self.size)] for _ in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):
                if not self.cells[row][col].isEmpty():
                    board[row][col] = self.cells[row][col].symbol
        for pos in self.O_positions:
            row, col = pos
            if board[row][col] == 'X':
                board[row][col] = 'O'
        for row in board:
            print(" ".join(row))

    def cellInBounds(self, cell):
        return 0 <= cell.position[0] < self.size and 0 <= cell.position[1] < self.size

    def InBounds(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size

    def getCellNeighbors(self, cell: Cell):
        directions = [
            ('up', [cell.position[0] - 1, cell.position[1]]),
            ('down', [cell.position[0] + 1, cell.position[1]]),
            ('right', [cell.position[0], cell.position[1] + 1]),
            ('left', [cell.position[0], cell.position[1] - 1])
        ]
        neighbors = []
        for direction, pos in directions:
            if self.cellInBounds(Cell(cell.color, pos)):
                neighbor_cell = self.cells[pos[0]][pos[1]]
                neighbors.append([direction, pos, neighbor_cell.symbol])
        return neighbors

    def stillCircles(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.cells[row][col].symbol == "O":
                    return False
        return True

    def checkIfBoardSolved(self):
        if not self.stillCircles():
            return False
        return True

    def getRedPossibleMoves(self):
        red_cell = self.findRedCell()
        red_moves = []
        if not red_cell:
            return
        red_moves.append([red_cell.position[0], red_cell.position[1]])
        for row in range(self.size):
            for col in range(self.size):
                if self.cells[row][col].symbol in ['X', 'O']:
                    red_moves.append([row, col])
        return red_moves

    def getPurplePossibleMoves(self):
        purple_cell = self.findPurpleCell()
        purple_moves = []
        if not purple_cell:
            return
        purple_moves.append([purple_cell.position[0], purple_cell.position[1]])
        for row in range(self.size):
            for col in range(self.size):
                if self.cells[row][col].symbol in ['X', 'O']:
                    purple_moves.append([row, col])
        return purple_moves

    def generateNewRedBoards(self):
        red_possible_moves = self.getRedPossibleMoves()
        result = []
        if not red_possible_moves:
            return
        for move in red_possible_moves:
            new_board = self.copy()
            new_red_cell = new_board.findRedCell()
            new_board.moveCell(new_red_cell, move[0], move[1])
            new_board.redCellAttraction()
            result.append(new_board)
        return result

    def generateNewPurpleBoards(self):
        purple_possible_moves = self.getPurplePossibleMoves()
        result = []
        if not purple_possible_moves:
            return
        for move in purple_possible_moves:
            new_board = self.copy()
            new_purple_cell = new_board.findPurpleCell()
            new_board.moveCell(new_purple_cell, move[0], move[1])
            new_board.purpleCellRepulsion()
            result.append(new_board)
        return result

    def redCellAttraction(self):
        red_cell = self.findRedCell()
        red_row, red_col = self.getCellRowAndColumn(red_cell)
        metal_in_row = None
        metal_in_col = None
        new_m_pos = []
        new_m_pos2 = []

        for r in red_row:
            if r.color != 'metal':
                continue
            else:
                metal_in_row = r
                break
        if metal_in_row is not None:
            if metal_in_row.position[1] > red_cell.position[1]:
                new_m_pos = [metal_in_row.position[0],
                             metal_in_row.position[1] - 1]
            else:
                new_m_pos = [metal_in_row.position[0],
                             metal_in_row.position[1] + 1]

            if 0 <= new_m_pos[0] < self.size and 0 <= new_m_pos[1] < self.size:
                if self.cells[new_m_pos[0]][new_m_pos[1]].symbol in ['X', 'O']:
                    self.moveCell(metal_in_row, new_m_pos[0], new_m_pos[1])
                    metal_in_row.setPosition(new_m_pos)

        for c in red_col:
            if c.color != 'metal':
                continue
            else:
                metal_in_col = c
                break
        if metal_in_col is not None:
            if metal_in_col.position[0] > red_cell.position[0]:
                new_m_pos2 = [metal_in_col.position[0] -
                              1, metal_in_col.position[1]]
            else:
                new_m_pos2 = [metal_in_col.position[0] +
                              1, metal_in_col.position[1]]

            if 0 <= new_m_pos2[0] < self.size and 0 <= new_m_pos2[1] < self.size:
                if self.cells[new_m_pos2[0]][new_m_pos2[1]].symbol in ['X', 'O']:
                    self.moveCell(metal_in_col, new_m_pos2[0], new_m_pos2[1])
                    metal_in_col.setPosition(new_m_pos2)

        return new_m_pos, new_m_pos2

    def purpleCellRepulsion(self):
        purple_cell = self.findPurpleCell()
        purple_row, purple_col = self.getCellRowAndColumn(purple_cell)
        metal_in_row = None
        metal_in_col = None
        new_m_pos = []
        new_m_pos2 = []

        for r in purple_row:
            if r.color != 'metal':
                continue
            else:
                metal_in_row = r
                break
        if metal_in_row is not None:
            if metal_in_row.position[1] > purple_cell.position[1]:
                new_m_pos = [metal_in_row.position[0],
                             metal_in_row.position[1] + 1]
            else:
                new_m_pos = [metal_in_row.position[0],
                             metal_in_row.position[1] - 1]

            if 0 <= new_m_pos[0] < self.size and 0 <= new_m_pos[1] < self.size:
                if self.cells[new_m_pos[0]][new_m_pos[0]].symbol in ['X', 'O']:
                    self.moveCell(metal_in_row, new_m_pos[0], new_m_pos[1])
                    metal_in_row.setPosition(new_m_pos)

        for c in purple_col:
            if c.color != 'metal':
                continue
            else:
                metal_in_col = c
                break
        if metal_in_col is not None:
            if metal_in_col.position[0] > purple_cell.position[0]:
                new_m_pos2 = [metal_in_col.position[0] +
                              1, metal_in_col.position[1]]
            else:
                new_m_pos2 = [metal_in_col.position[0] -
                              1, metal_in_col.position[1]]

            if 0 <= new_m_pos2[0] < self.size and 0 <= new_m_pos2[1] < self.size:
                if self.cells[new_m_pos2[0]][new_m_pos2[0]].symbol in ['X', 'O']:
                    self.moveCell(metal_in_col, new_m_pos2[0], new_m_pos2[1])
                    metal_in_col.setPosition(new_m_pos2)

        return new_m_pos, new_m_pos2

    def copy(self):
        new_board = Board(self.size)
        new_board.cells = [[Cell(cell.color, cell.position[:])
                            for cell in row] for row in self.cells]
        new_board.O_positions = [pos[:] for pos in self.O_positions]
        return new_board

    def generateNewBoardsForNeighbors(self):
        red_cell = self.findRedCell()
        purple_cell = self.findPurpleCell()
        red_boards = None
        purple_boards = None
        if red_cell:
            red_neighbors = self.getCellNeighbors(red_cell)
        else:
            red_neighbors = None
        if purple_cell:
            purple_neighbors = self.getCellNeighbors(purple_cell)
        else:
            purple_neighbors = None
        if red_neighbors:
            red_boards = []
            for neighbor in red_neighbors:
                new_board = self.copy()
                new_red = new_board.findRedCell()
                new_board.moveCell(new_red, neighbor[1][0], neighbor[1][1])
                new_board.redCellAttraction()
                red_boards.append(new_board)
        if purple_neighbors:
            purple_boards = []
            for neighbor in purple_neighbors:
                new_board = self.copy()
                new_purple = new_board.findPurpleCell()
                new_board.moveCell(new_purple, neighbor[1][0], neighbor[1][1])
                new_board.purpleCellRepulsion()
                purple_boards.append(new_board)
        return red_boards, purple_boards
