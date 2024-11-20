from newBoard import Board
from TreeNode import TreeNode

class State:
    def __init__(self, initial_board: Board):
        self.current_board = initial_board
        self.root_state = TreeNode(initial_board)

    def addStateChildToRootState(self, child_board):
        child_state = State(child_board)
        self.root_state.addChild(child_state)
        return self

    def createNewStatesFromNewBoardsAndAddToRootChildren(self):
        new_red_boards = self.current_board.generateNewRedBoards()
        new_purple_boards = self.current_board.generateNewPurpleBoards()
        if new_red_boards:
            for board in new_red_boards:
                child_state = State(board)
                self.root_state.addChild(TreeNode(child_state))
        elif new_purple_boards:
            for board in new_purple_boards:
                child_state = State(board)
                self.root_state.addChild(TreeNode(child_state))
        return self
    
    def createNewStatesFromNeighborsAndAddToRootChildren(self):
        new_red_boards, new_purple_boards = self.current_board.generateNewBoardsForNeighbors()
        if new_red_boards:
            for board in new_red_boards:
                child_state = State(board)
                self.root_state.addChild(TreeNode(child_state))
        elif new_purple_boards:
            for board in new_purple_boards:
                child_state = State(board)
                self.root_state.addChild(TreeNode(child_state))
        return self