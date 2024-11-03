from Board import Board
from State import State
from Levels import Levels
from Levels import level


def dfs(initial_state: Board):
    tries = 3
    print("solving using dfs algorithm:")

    stack = [(initial_state, tries)]
    explored_set = set()

    while stack:
        current_board, current_tries = stack.pop()

        if current_tries <= 0:
            continue

        print("try: ", current_tries)
        current_board.print_board()
        print()

        if current_board.check_if_board_solved():
            print("Goal State found with tries left:", current_tries)
            current_board.print_board()
            return current_board

        explored_set.add(current_board)

        state = State(current_tries, current_board)
        state.get_possible_mixed_moves_from_board(current_board)
        state.generate_mixed_new_boards_and_add_to_neighbors(current_board)

        for neighbor in state.graph.get_neighbors(current_board):
            print("\tNeighbor board with tries left:", current_tries - 1)
            neighbor.print_board()

            if neighbor not in explored_set:
                stack.append((neighbor, current_tries - 1))
                print("\tAdding neighbor to stack")
                neighbor.print_board()
                print()

                if neighbor.check_if_board_solved():
                    print("Goal State found with tries left:", current_tries - 1)
                    neighbor.print_board()
                    return neighbor

        print("Stack length after iteration:", len(stack))
    print("No solution found")

def play():
    i = 3
    num = input("Enter a level: ")
    while i > 0:
        level_num = int(num)
        if 1 <= level_num <= len(Levels):
            level(Levels[level_num-1]).print_board()
            magnet = input("purple or red: ")
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            if magnet == "purple":
                if level(Levels[level_num-1]).neg is not None:
                    level(
                        Levels[level_num-1]).move_cell(level(Levels[level_num-1]).neg, [int(row), int(col)])
                else:
                    print("No purple magnet to move!")
            elif magnet == "red":
                if level(Levels[level_num-1]).pos is not None:
                    level(
                        Levels[level_num-1]).move_cell(level(Levels[level_num-1]).pos, [int(row), int(col)])
                else:
                    print("No red magnet to move!")
            print()
            if level(Levels[level_num-1]).check_if_board_solved():
                print("You Won :)")
                level(Levels[level_num-1]).print_board()
                break
            else:
                if i == 1:
                    print("You Lost :(")
                    level(Levels[level_num-1]).print_board()
                    break
                else:
                    print("Continue")
                    level(Levels[level_num-1]).print_board()
                    print()
                    i -= 1
                    print("Tries left: ", i)
        else:
            print("Invalid level number")
            break


type = input("Play or DFS? ")
if type == "play":
    play()
elif type == "dfs":
    level_chosen = input("Choose a level from 1 to 25: ")
    board = level(Levels[int(level_chosen)-1])
    board.print_board()
    result = dfs(board)
    if result:
        print("DFS algo found a solution")
    else:
        print("No solution found")
