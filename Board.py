from Node import Node


class Board:
    def __init__(self, n, neg=None, pos=None):
        self.n = n
        self.board = self.init_board()
        self.circle_positions = self.see_circle_positions()
        self.neg = neg
        self.pos = pos
        if neg:
            neg.set_cell(self.board)
        if pos:
            pos.set_cell(self.board)

    def init_board(self):
        board = []
        for row in range(self.n):
            board_row = []
            for col in range(self.n):
                board_row.append(Node("empty", [row, col]))
            board.append(board_row)
        return board

    def print_board(self):
        for row in self.board:
            print("  ".join(node.symbol for node in row))

    def see_circle_positions(self):
        positions = []
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col].symbol == "O":
                    positions.append((row, col))
        return positions

    def diff_between_cell(self, node1, node2):
        return [abs(node2.position[0] - node1.position[0]) - 1, abs(node2.position[1] - node1.position[1]) - 1]

    def get_all_nodes_diffs(self, node):
        res = []
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col].symbol == "X":
                    continue
                else:
                    res.append([row, col, self.board[row][col].symbol,
                               self.diff_between_cell(node, Node("O", [row, col]))])
        return res

    def node_in_bounds(self, node):
        return 0 <= node.position[0] < self.n and 0 <= node.position[1] < self.n

    def get_node_neighbors(self, node: Node):
        directions = [
            ('up', [node.position[0] - 1, node.position[1]]),
            ('down', [node.position[0] + 1, node.position[1]]),
            ('right', [node.position[0], node.position[1] + 1]),
            ('left', [node.position[0], node.position[1] - 1])
        ]
        neighbors = []
        for direction, pos in directions:
            if self.node_in_bounds(Node(node.color, pos)):
                neighbor_node = self.board[pos[0]][pos[1]]
                if isinstance(neighbor_node, Node):
                    neighbors.append([direction, pos, neighbor_node.symbol])
        return neighbors

    def check_circle_cells_positions(self):
        for pos in self.see_circle_positions():
            if self.board[pos[0]][pos[1]].symbol not in ["M", "+", "-"]:
                return False
        return True

    def still_circles(self):
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col].symbol == "O":
                    return False
        return True

    def check_if_board_solved(self):
        if not self.still_circles() or not self.check_circle_cells_positions():
            return False
        return True

    def move_cell(self, node: Node, new_pos):
        target_cell = self.board[new_pos[0]][new_pos[1]]
        if target_cell.symbol == "X" or target_cell.symbol == "O":
            self.board[node.position[0]][node.position[1]] = Node(
                "empty", node.position)
            node.position = new_pos
            self.board[new_pos[0]][new_pos[1]] = node
            node.has_circle_previous = (target_cell.symbol == "O")
        if node.color == "red":
            self.move_red_action(new_pos)
        elif node.color == "purple":
            self.move_purple_action(new_pos)

    def copy(self):
        new_board = Board(self.n)
        new_board.board = [[Node(node.color, node.position[:])
                            for node in row] for row in self.board]
        new_board.circle_positions = [pos[:] for pos in self.circle_positions]
        return new_board

    def have_M_neighbors(self, node: Node):
        neighbors = self.get_node_neighbors(node)
        res = []
        for neighbor in neighbors:
            if neighbor[-1] == "M":
                res.append(neighbor)
        return res

    def move_purple_action(self, newpos: list):
        newrow = newpos[0]
        newcol = newpos[1]
        size = self.n

        for r in range(size):
            if isinstance(self.board[newrow][r], Node) and self.board[newrow][r].symbol in ["M", "+"]:
                node = Node.get_node_at_position(self.board, [newrow, r])
                if node:
                    if r > newcol:
                        if r + 1 < size and self.board[newrow][r + 1].symbol in ["X", "O"]:
                            newmovedposlist = [newrow, r + 1]
                            self.board[newrow][r] = Node("empty", [newrow, r])
                            self.board[newrow][r + 1] = node
                            node.position = newmovedposlist
                            break
                    else:
                        if r - 1 >= 0 and self.board[newrow][r - 1].symbol in ["X", "O"]:
                            newmovedposlist = [newrow, r - 1]
                            self.board[newrow][r] = Node("empty", [newrow, r])
                            self.board[newrow][r - 1] = node
                            node.position = newmovedposlist

        for c in range(size):
            if isinstance(self.board[c][newcol], Node) and self.board[c][newcol].symbol in ["M", "+"]:
                node = Node.get_node_at_position(self.board, [c, newcol])
                if node:
                    if c > newrow:
                        if c + 1 < size and self.board[c + 1][newcol].symbol in ["X", "O"]:
                            newmovedposlist = [c + 1, newcol]
                            self.board[c][newcol] = Node("empty", [c, newcol])
                            self.board[c + 1][newcol] = node
                            node.position = newmovedposlist
                            break
                    else:
                        if c - 1 >= 0 and self.board[c - 1][newcol].symbol in ["X", "O"]:
                            newmovedposlist = [c - 1, newcol]
                            self.board[c][newcol] = Node("empty", [c, newcol])
                            self.board[c - 1][newcol] = node
                            node.position = newmovedposlist

    def move_red_action(self, newpos: list):
        newrow = newpos[0]
        newcol = newpos[1]
        size = self.n

        for r in range(size):
            if isinstance(self.board[newrow][r], Node) and self.board[newrow][r].symbol in ["M", "-"]:
                node = Node.get_node_at_position(self.board, [newrow, r])
                if node:
                    if r < newcol:
                        if r + 1 < size and self.board[newrow][r + 1].symbol in ["X", "O"]:
                            newmovedposlist = [newrow, r + 1]
                            self.board[newrow][r] = Node("empty", [newrow, r])
                            self.board[newrow][r + 1] = node
                            node.position = newmovedposlist
                    else:
                        if r - 1 >= 0 and self.board[newrow][r - 1].symbol in ["X", "O"]:
                            newmovedposlist = [newrow, r - 1]
                            self.board[newrow][r] = Node("empty", [newrow, r])
                            self.board[newrow][r - 1] = node
                            node.position = newmovedposlist
                            break

        for c in range(size):
            if isinstance(self.board[c][newcol], Node) and self.board[c][newcol].symbol in ["M", "-"]:
                node = Node.get_node_at_position(self.board, [c, newcol])
                if node:
                    if c < newrow:
                        if c + 1 < size and self.board[c + 1][newcol].symbol in ["X", "O"]:
                            newmovedposlist = [c + 1, newcol]
                            self.board[c][newcol] = Node("empty", [c, newcol])
                            self.board[c + 1][newcol] = node
                            node.position = newmovedposlist
                    else:
                        if c - 1 >= 0 and self.board[c - 1][newcol].symbol in ["X", "O"]:
                            newmovedposlist = [c - 1, newcol]
                            self.board[c][newcol] = Node("empty", [c, newcol])
                            self.board[c - 1][newcol] = node
                            node.position = newmovedposlist
                            break
