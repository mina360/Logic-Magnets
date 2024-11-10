from collections import deque
from newState import State
from newBoard import Board


board_one = Board(3)
red = board_one.setCell(1, 0, 'red')
board_one.setCell(2, 2, 'metal')
board_one.setCell(2, 0, 'white')
board_one.setCell(2, 1, 'white')

board_two = Board(4)
purple = board_two.setCell(0, 0, 'purple')
board_two.setCell(2, 1, 'metal')
board_two.setCell(2, 0, 'white')
board_two.setCell(2, 2, 'white')

board_four = Board(4)
red4 = board_four.setCell(0, 0, 'red')
board_four.setCell(1, 2, 'metal')
board_four.setCell(2, 0, 'white')
board_four.setCell(2, 1, 'white')

# 14
board_14 = Board(4)
red = board_14.setCell(3, 3, 'red')
board_14.setCell(0, 3, 'metal')
board_14.setCell(2, 0, 'metal')
board_14.setCell(3, 0, 'metal')
board_14.setCell(1, 0, 'white')
board_14.setCell(1, 2, 'white')
board_14.setCell(2, 1, 'white')
board_14.setCell(2, 2, 'white')

# 12
board_12 = Board(5)
red = board_12.setCell(3, 1, 'red')
board_12.setCell(0, 0, 'metal')
board_12.setCell(1, 0, 'metal')
board_12.setCell(4, 3, 'metal')
board_12.setCell(2, 0, 'white')
board_12.setCell(4, 0, 'white')
board_12.setCell(4, 2, 'white')

def dfs(initial_state: State):
    print('solving using DFS algo: ')
    stack = [initial_state]
    explored_set = set()
    iteration_count = 0
    while stack:
        iteration_count += 1
        current_state = stack.pop()
        print(f"Iteration: {iteration_count}")
        print('current board: ')
        current_state.current_board.printBoard()
        print()
        if current_state.current_board.checkIfBoardSolved():
            print("Goal State found: ")
            current_state.current_board.printBoard()
            return current_state
        explored_set.add(current_state)
        # current_state.createNewStatesFromNeighborsAndAddToRootChildren()
        current_state.createNewStatesFromNewBoardsAndAddToRootChildren()
        for child in current_state.root_state.children:
            child_state = child.value
            if child_state not in explored_set:
                stack.append((child_state))
                print('New child board:')
                # print(child_state.current_board)
                child_state.current_board.printBoard()
                print()
                if child_state.current_board.checkIfBoardSolved():
                    print("Goal State found: ")
                    child_state.current_board.printBoard()
                    return child
    print("No solution found")
    return None

def bfs(initial_state: State):
    print('solving using BFS algo: ')
    queue = deque([initial_state])
    explored_set = set()
    iteration_count = 0
    while queue:
        iteration_count += 1
        current_state = queue.popleft()
        print(f"Iteration: {iteration_count}")
        print('current board: ')
        current_state.current_board.printBoard()
        print()
        if current_state.current_board.checkIfBoardSolved():
            print("Goal State found: ")
            current_state.current_board.printBoard()
            return current_state
        explored_set.add(current_state.current_board)
        # current_state.createNewStatesFromNewBoardsAndAddToRootChildren()
        current_state.createNewStatesFromNewBoardsAndAddToRootChildren()
        for child in current_state.root_state.children:
            child_state = child.value
            if child_state.current_board not in explored_set:
                queue.append(child_state)
                print('New child board:')
                child_state.current_board.printBoard()
                print()
                if child_state.current_board.checkIfBoardSolved():
                    print("Goal State found: ")
                    child_state.current_board.printBoard()
                    return child
    print("No solution found")
    return None

level = input('enter a level: ')
choice = input('Dfs or Bfs: ')
if level == '1':
    initial_state = State(board_one)
    board_one.printBoard()
    print()
    if choice == 'dfs':
        result_state = dfs(initial_state)
    elif choice == 'bfs':
        result_state = bfs(initial_state)
elif level == '2':
    initial_state = State(board_two)
    board_two.printBoard()
    print()
    if choice == 'dfs':
        result_state = dfs(initial_state)
    elif choice == 'bfs':
        result_state = bfs(initial_state)
elif level == '3':
    initial_state = State(board_four)
    board_four.printBoard()
    print()
    if choice == 'dfs':
        result_state = dfs(initial_state)
    elif choice == 'bfs':
        result_state = bfs(initial_state)
elif level == '14':
    initial_state = State(board_14)
    board_14.printBoard()
    print()
    if choice == 'dfs':
        result_state = dfs(initial_state)
    elif choice == 'bfs':
        result_state = bfs(initial_state)
elif level == '12':
    initial_state = State(board_12)
    board_12.printBoard()
    print()
    if choice == 'dfs':
        result_state = dfs(initial_state)
    elif choice == 'bfs':
        result_state = bfs(initial_state)