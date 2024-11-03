from Graph import Graph
from Board import Board
from Node import Node


class State:
    def __init__(self, tries_left, initial_board: Board):
        self.tries_left = tries_left
        self.red_possible_moves = []
        self.purple_possible_moves = []
        self.current_board = initial_board
        self.root_state = self.initialize_root_state(initial_board)

    def initialize_root_state(self, root_board):
        self.graph = Graph()
        self.graph.add_board(root_board)
        return root_board

    def get_possible_moves_from_board(self, current_board):
        red_pos = []
        purple_pos = []
        for row in range(current_board.n):
            for col in range(current_board.n):
                if current_board.board[row][col].symbol == "+":
                    red_pos = [row, col]
                elif current_board.board[row][col].symbol == "-":
                    purple_pos = [row, col]

        for row in range(current_board.n):
            for col in range(current_board.n):
                if current_board.board[row][col].symbol == "X" or current_board.board[row][col].symbol == "O":
                    if red_pos:
                        self.red_possible_moves.append([row, col])
                    if purple_pos:
                        self.purple_possible_moves.append([row, col])

        return self.red_possible_moves, self.purple_possible_moves

    def generate_purple_new_boards_and_add_to_neighbors(self, current_board: Board):
        purple_pos = []
        for row in range(current_board.n):
            for col in range(current_board.n):
                if current_board.board[row][col].symbol == "-":
                    purple_pos = [row, col]

        if purple_pos and self.purple_possible_moves:
            for move in self.purple_possible_moves:
                new_board = current_board.copy()
                purple_node = Node("purple", purple_pos)
                new_board.move_cell(purple_node, move)
                self.graph.add_board(new_board)
                self.graph.add_edge(self.root_state, new_board)

    def generate_red_new_boards_and_add_to_neighbors(self, current_board: Board):
        red_pos = []
        for row in range(current_board.n):
            for col in range(current_board.n):
                if current_board.board[row][col].symbol == "+":
                    red_pos = [row, col]

        if red_pos and self.red_possible_moves:
            for move in self.red_possible_moves:
                new_board = current_board.copy()
                red_node = Node("red", red_pos)
                new_board.move_cell(red_node, move)
                self.graph.add_board(new_board)
                self.graph.add_edge(self.root_state, new_board)

    def get_possible_mixed_moves_from_board(self, current_board: Board):
        possible_red_moves, possible_purple_moves = self.get_possible_moves_from_board(
            current_board)
        mix_possible_moves_starting_red = []
        mix_possible_moves_starting_purple = []
        res_set_red = set()
        res_set_purple = set()
        for i in range(int((len(possible_red_moves) + len(possible_purple_moves))/2)):
            #* start red
            if possible_red_moves:
                mix_possible_moves_starting_red.append(possible_red_moves[i])
            if possible_purple_moves:
                mix_possible_moves_starting_red.append(possible_purple_moves[i])
            #* start purple
            if possible_purple_moves:
                mix_possible_moves_starting_purple.append(possible_purple_moves[i])
            if possible_red_moves:
                mix_possible_moves_starting_purple.append(possible_red_moves[i])
        for list in mix_possible_moves_starting_red:
            res_set_red.add(tuple(list))
        for list in mix_possible_moves_starting_purple:
            res_set_purple.add(tuple(list))
        return res_set_red, res_set_purple

    def generate_mixed_new_boards_and_add_to_neighbors11(self, current_board: Board):
        start_red, start_purple = self.get_possible_mixed_moves_from_board(current_board)
        for i in range(int((len(start_red) + len(start_purple))/2)):
            #* Start red
            if i < len(start_red):
                new_board = current_board.copy()
                red_node = Node.get_node_at_position(new_board.board, current_board.pos.position)
                # print("moveing red to ", start_red[i])
                new_board.move_cell(red_node, start_red[i])
                self.graph.add_board(new_board)
                self.graph.add_edge(self.root_state, new_board)

                if i < len(start_purple):
                    newer_board = new_board.copy()
                    purple_node = Node.get_node_at_position(newer_board.board, current_board.neg.position)
                    # print("moveing purple to ", start_purple[i])
                    newer_board.move_cell(purple_node, start_purple[i])
                    self.graph.add_board(newer_board)
                    self.graph.add_edge(self.root_state, newer_board)

            #* Start purple
            if i < len(start_purple):
                new_board = current_board.copy()
                purple_node = Node.get_node_at_position(new_board.board, current_board.neg.position)
                # print("moveing purple to ", start_purple[i])
                new_board.move_cell(purple_node, start_purple[i])
                self.graph.add_board(new_board)
                self.graph.add_edge(self.root_state, new_board)

                if i < len(start_red):
                    newer_board = new_board.copy()
                    red_node = Node.get_node_at_position(newer_board.board, current_board.pos.position)
                    # print("moveing red to ", start_red[i])
                    newer_board.move_cell(red_node, start_red[i])
                    self.graph.add_board(newer_board)
                    self.graph.add_edge(self.root_state, newer_board)


    def generate_mixed_new_boards_and_add_to_neighbors(self, current_board: Board):
        if current_board.pos is None:
            self.generate_purple_new_boards_and_add_to_neighbors(current_board)
            return
        elif current_board.neg is None:
            self.generate_red_new_boards_and_add_to_neighbors(current_board)
            return

        start_red, start_purple = self.get_possible_mixed_moves_from_board(current_board)
        start_red = list(start_red)
        start_purple = list(start_purple)

        for i in range(int((len(start_red) + len(start_purple))/2)):
            #* Start red
            if i < len(start_red) and (i+1) < len(start_purple):
                new_board = current_board.copy()
                purple_node = Node.get_node_at_position(new_board.board, current_board.neg.position)
                red_node = Node.get_node_at_position(new_board.board, current_board.pos.position)
                new_board.move_cell(red_node, start_red[i])
                new_board.move_cell(purple_node, start_purple[i+1])
                self.graph.add_board(new_board)
                self.graph.add_edge(self.root_state, new_board)

            #* Start purple
            if i < len(start_purple) and (i+1) < len(start_red):
                new_board = current_board.copy()
                purple_node = Node.get_node_at_position(new_board.board, current_board.neg.position)
                red_node = Node.get_node_at_position(new_board.board, current_board.pos.position)
                new_board.move_cell(purple_node, start_purple[i])
                new_board.move_cell(red_node, start_red[i+1])
                self.graph.add_board(new_board)
                self.graph.add_edge(self.root_state, new_board)
