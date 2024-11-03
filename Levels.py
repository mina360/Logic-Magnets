from Board import Board
from Node import Node


def level(level):
    board_no = level[0]
    for i in range(len(level)):
        if i == 0:
            continue
        level[i].set_cell(board_no.board)
    return board_no


Levels = [
    [
        # * level 1
        Board(4, Node("purple", [2, 0]), None),
        Node("white", [1, 1]),
        Node("white", [1, 3]),
        Node("metal", [1, 2]),
    ],
    [
        # * level 2
        Board(5, Node("purple", [4, 0]), None),
        Node("metal", [1, 2]),
        Node("metal", [2, 1]),
        Node("metal", [2, 3]),
        Node("metal", [3, 2]),
        Node("white", [0, 2]),
        Node("white", [2, 0]),
        Node("white", [2, 2]),
        Node("white", [2, 4]),
        Node("white", [4, 2]),
    ],
    [
        # ! level 3
        Board(4, Node("purple", [2, 0]), None),
        Node("metal", [1, 2]),
        Node("white", [0, 3]),
        Node("white", [2, 3]),
    ],
    [
        # ! level 4
        Board(5, Node("purple", [2, 1]), None),
        Node("metal", [1, 2]),
        Node("metal", [3, 2]),
        Node("white", [0, 1]),
        Node("white", [0, 3]),
        Node("white", [4, 2]),
    ],
    [
        # * level 5
        Board(4, Node("purple", [3, 1]), None),
        Node("metal", [1, 0]),
        Node("metal", [1, 2]),
        Node("metal", [2, 2]),
        Node("metal", [2, 0]),
        Node("white", [1, 0]),
        Node("white", [0, 0]),
        Node("white", [0, 2]),
        Node("white", [1, 2]),
        Node("white", [3, 0]),
    ],
    [
        # ! level 6
        Board(5, Node("purple", [3, 0]), None),
        Node("metal", [2, 1]),
        Node("metal", [2, 3]),
        Node("white", [2, 2]),
        Node("white", [1, 3]),
        Node("white", [3, 3]),
    ],
    [
        # ! level 7
        Board(5, Node("purple", [2, 1]), None),
        Node("metal", [1, 0]),
        Node("metal", [2, 0]),
        Node("metal", [3, 1]),
        Node("metal", [3, 2]),
        Node("white", [0, 0]),
        Node("white", [1, 0]),
        Node("white", [2, 3]),
        Node("white", [3, 2]),
        Node("white", [4, 3]),
    ],
    [
        # * level 8
        Board(4, Node("purple", [3, 0]), None),
        Node("metal", [2, 2]),
        Node("metal", [2, 1]),
        Node("white", [1, 2]),
        Node("white", [1, 0]),
        Node("white", [3, 2]),
    ],
    [
        # ! level 9
        Board(7, Node("purple", [3, 0]), None),
        Node("metal", [3, 3]),
        Node("metal", [3, 5]),
        Node("white", [3, 1]),
        Node("white", [3, 3]),
        Node("white", [3, 6]),
    ],
    [
        # * level 10
        Board(4, Node("purple", [0, 0]), None),
        Node("metal", [3, 1]),
        Node("metal", [2, 2]),
        Node("metal", [2, 3]),
        Node("white", [1, 1]),
        Node("white", [3, 0]),
        Node("white", [3, 3]),
        Node("white", [1, 3]),
    ],
    [
        #  level 11
        Board(5, None, Node("red", [2, 2])),
        Node("metal", [1, 0]),
        Node("metal", [1, 4]),
        Node("white", [1, 1]),
        Node("white", [1, 2]),
        Node("white", [1, 3]),
    ],
    [
        # * level 12
        Board(5, None, Node("red", [3, 1])),
        Node("metal", [0, 0]),
        Node("metal", [1, 0]),
        Node("metal", [4, 3]),
        # Node("white", [1, 0]),
        Node("white", [2, 0]),
        Node("white", [4, 0]),
        Node("white", [4, 2]),
    ],
    [
        #  level 13
        Board(6, None, Node("red", [4, 3])),
        Node("metal", [2, 0]),
        Node("metal", [2, 4]),
        Node("metal", [2, 5]),
        Node("white", [2, 3]),
        Node("white", [2, 4]),
        Node("white", [2, 5]),
        Node("white", [3, 1]),
        Node("white", [4, 1]),
    ],
    [
        #  level 14
        Board(4, None, Node("red", [3, 3])),
        Node("metal", [0, 3]),
        Node("metal", [2, 0]),
        Node("metal", [3, 0]),
        Node("white", [1, 0]),
        Node("white", [1, 2]),
        Node("white", [2, 1]),
        Node("white", [2, 2]),
    ],
    [
        # ! level 15
        Board(5, Node("purple", [2, 2]), Node("red", [3, 2])),
        Node("metal", [1, 1]),
        Node("metal", [1, 3]),
        Node("white", [1, 0]),
        Node("white", [1, 2]),
        Node("white", [2, 4]),
        Node("white", [3, 4]),
    ],
    [
        # ! level 16
        Board(5, Node("purple", [2, 4]), Node("red", [2, 0])),
        Node("metal", [1, 2]),
        Node("metal", [3, 2]),
        Node("white", [0, 3]),
        Node("white", [0, 4]),
        Node("white", [4, 0]),
        Node("white", [4, 3]),
    ],
    [
        # ! level 17
        Board(4, Node("purple", [3, 3]), Node("red", [0, 0])),
        Node("white", [1, 1]),
        Node("white", [1, 3]),
        Node("white", [2, 2]),
        Node("white", [3, 1]),
        Node("metal", [0, 2]),
        Node("metal", [2, 0]),
    ],
    [
        # ! level 18
        Board(6, Node("purple", [5, 3]), Node("red", [5, 2])),
        Node("metal", [3, 0]),
        Node("metal", [1, 3]),
        Node("metal", [3, 5]),
        Node("white", [2, 3]),
        Node("white", [3, 1]),
        Node("white", [3, 2]),
        Node("white", [3, 3]),
        Node("white", [3, 5]),
    ],
    [
        # ! level 19
        Board(5, Node("purple", [0, 2]), Node("red", [2, 2])),
        Node("metal", [0, 1]),
        Node("metal", [0, 3]),
        Node("metal", [4, 1]),
        Node("metal", [4, 3]),
        Node("white", [1, 0]),
        Node("white", [1, 4]),
        Node("white", [2, 1]),
        Node("white", [3, 0]),
        Node("white", [3, 2]),
        Node("white", [3, 4]),
    ],
    [
        # ! level 20
        Board(5, Node("purple", [4, 2]), Node("red", [4, 3])),
        Node("metal", [0, 1]),
        Node("metal", [0, 2]),
        Node("metal", [4, 0]),
        Node("white", [0, 1]),
        Node("white", [0, 3]),
        Node("white", [1, 0]),
        Node("white", [2, 0]),
        Node("white", [3, 0]),
    ],
    [
        # ! level 21
        Board(4, Node("purple", [3, 0]), Node("red", [3, 3])),
        Node("metal", [1, 1]),
        Node("metal", [2, 1]),
        Node("metal", [2, 2]),
        Node("white", [2, 0]),
        Node("white", [2, 1]),
        Node("white", [1, 2]),
        Node("white", [3, 0]),
        Node("white", [3, 1]),
    ],
    [
        # ! level 22
        Board(5, Node("purple", [0, 0]), Node("red", [3, 2])),
        Node("metal", [0, 3]),
        Node("metal", [0, 4]),
        Node("metal", [3, 0]),
        Node("white", [0, 1]),
        Node("white", [0, 3]),
        Node("white", [1, 0]),
        Node("white", [1, 4]),
        Node("white", [2, 1]),
    ],
    [
        # ! level 23
        Board(5, Node("purple", [3, 4]), Node("red", [3, 2])),
        Node("metal", [0, 3]),
        Node("metal", [1, 4]),
        Node("metal", [2, 0]),
        Node("white", [0, 2]),
        Node("white", [2, 1]),
        Node("white", [2, 2]),
        Node("white", [2, 3]),
    ],
    [
        # ! level 24
        Board(5, Node("purple", [1, 4]), Node("red", [3, 0])),
        Node("metal", [0, 1]),
        Node("metal", [1, 3]),
        Node("metal", [3, 4]),
        Node("white", [0, 3]),
        Node("white", [2, 1]),
        Node("white", [2, 3]),
        Node("white", [4, 1]),
        Node("white", [4, 2]),
    ],
    [
        # ! level 25
        Board(5, Node("purple", [4, 0]), Node("red", [0, 3])),
        Node("metal", [4, 3]),
        Node("metal", [1, 2]),
        Node("metal", [3, 2]),
        Node("white", [0, 0]),
        Node("white", [0, 3]),
        Node("white", [2, 0]),
        Node("white", [4, 0]),
        Node("white", [4, 1]),
        Node("white", [4, 2]),
    ],
]