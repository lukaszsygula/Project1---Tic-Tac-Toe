#!/usr/bin/env python
# coding: utf-8

# In[1]:


def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, mark):
    for row in board:
        if all(cell == mark for cell in row):
            return True

    for col in range(3):
        if all(row[col] == mark for row in board):
            return True

    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        display_board(board)
        row = int(input(f"Player {current_player}, choose a row (0-2): "))
        col = int(input(f"Player {current_player}, choose a column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player

            if check_win(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_full(board):
                display_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("This cell is already taken. Try again.")

if __name__ == "__main__":
    play_game()


# In[ ]:




